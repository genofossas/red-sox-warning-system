# Red Sox Warning System

This is a warning system that sends out text reminders the day there is a home game for the Boston Red Sox. I live along the green line, so it can really ruin my day if I don't know when there is a game, so I created this quick and dirty python script that reminds me so I don't forget to look.

I used the following:
- `icalendar` python library
- `pytextbelt` python library (in `pytextbelt.py`) adapted from [here]().
- `textbelt`: Provider for texting. You can pay them to get an API key, or you can self-host. More here: 

## Set-Up

If you want to use this software, you need to set a few things in a `.env` file in the root directory of this repository. These are:

1. `ICAL_URL`: The `https` url for the ical file of games (or whatever else you're using this for)
2. `RECIPIENT`: The phone number you're going to be sending the text to
3. `TEXTBELT_API_KEY`: The key you'll be providing to the textbelt API. You'll need to modify this for self-hosted instances.

From there you can schedule your cronjob to run it however many times you want. I have it run at 7am local time every day because that's before I get up.