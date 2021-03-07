from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from twilio.rest import Client

PATH = "/path/to/chromedriver"
driver = webdriver.Chrome(PATH)


def login():
    driver.get("https://ubc.perfectmind.com/")

    image = driver.find_element_by_tag_name("img").click()

    login_name = driver.find_element_by_id("username")
    login_name.send_keys("username")

    password = driver.find_element_by_id("password")
    password.send_keys("password")
    password.send_keys(Keys.RETURN)

    time.sleep(20)

    navigation = driver.find_element_by_xpath(
        '//*[@id="ApplicationMenu"]/li[4]/a'
    ).click()

    time.sleep(3)

    arc = driver.find_element_by_xpath(
        '//*[@id="bm-categories"]/div[1]/div/ul/li[1]/a'
    ).click()


# login()


def get_current_openings():
    curr_openings = []
    for x in range(1, 30):
        try:
            if (
                driver.find_element_by_xpath(
                    f'//*[@id="classes"]/tr[{x}]'
                ).get_attribute("class")
                == "bm-class-row"
            ):
                try:
                    if (
                        driver.find_element_by_xpath(
                            f'//*[@id="classes"]/tr[{x}]/td/div/div[2]/div[1]/span'
                        ).is_displayed()
                        and driver.find_element_by_xpath(
                            f'//*[@id="classes"]/tr[{x}]/td/div/div[2]/div[1]/span'
                        ).text
                        != "Full"
                    ):
                        time_slot = driver.find_element_by_xpath(
                            f'//*[@id="classes"]/tr[{x}]/td/div/div[3]/div[1]/span'
                        ).text
                        curr_openings.append(time_slot)
                        print("there's a spot apparently at " + time_slot)
                except:
                    print("element doesn't exist")
        except:
            print("table row doesn't exist")
    return curr_openings


account_sid = "sid"
auth_token = "token"
client = Client(account_sid, auth_token)

login()
while True:
    time.sleep(5)
    current_openings = get_current_openings()
    if len(current_openings) < 1:
        print("no openings yet")
    else:
        msg = ""
        for x in current_openings:
            msg = msg + x + "\n"
        print(msg)
        message = client.messages.create(
            messaging_service_sid="sid",
            body=msg,
            to="phone_number",
        )
    time.sleep(5)
    driver.refresh()