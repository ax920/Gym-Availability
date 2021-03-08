# Gym-Availability
A Python script that alerts you through text message when there is an open spot at the UBC gym.

It's 2020/2021, and COVID has made it so that you have to book a time online if you want to workout. 
Spots run out super quickly (< 1 min) when they are released,
so clearly we need a way to find open bookings at the gym. 
I wrote this bot that uses Selenium WebDriver to scrape PerfectMind's online booking system.
If it detects that there is an opening, it sends you a text message using the Twilio API.

# Directions

- If you're not on the sender list, ask me and I'll put you on!
- Text START to +18143245498 to start looking for availabilities. If there are availabilities, it will ping you every few second!
- When you have found a time or no longer wish to have texts sent to you every few seconds, text STOP.
- Get huge
