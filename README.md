# Red Sox Warning System

This is a warning system that sends out text reminders the day there is a home game for the Boston Red Sox. I use the MBTA frequently, so it can really ruin my day if I don't know there is a game. To solve this issue, I created this quick and dirty python script that reminds me. This ultimately saves me from Red Sox Train Suffering(tm).

I used the following:
- `icalendar` python library
- `pytextbelt` python library (in `pytextbelt.py`) adapted from [here](https://github.com/ksdme/py-textbelt/tree/master).
- `textbelt`: Provider for texting. You can pay them to get an API key, or you can self-host. [More here](https://textbelt.com/).

## Set-Up

If you want to use this software, you need to set a few things in a `.env` file in the root directory of this repository. These are:

1. `ICAL_URL`: The `https` url for the ical file of games (or whatever else you're using this for).
2. `RECIPIENT`: The phone number you're going to be sending the text to.
3. `TEXTBELT_API_KEY`: The key you'll be providing to the textbelt API. You'll need to modify how the code handles this manually for self-hosted instances.

From there you can schedule your cronjob to run it however many times you want. I have it run at 7am local time every day.

To run the code in cron:
1. Set up a python virtual environment: `python3 -m venv /path/to/proj/root/venv`
   - Activate the environment: `source /path/to/proj/root/venv/bin/activate`
   - Install dependencies: `pip install -r requirements.txt`
   - Exit the venv: `deactivate`
2. Add the following into your crontab (in the scripts field): `/path/to/proj/root/venv/bin/python /path/to/proj/root/red-sox-ward.py`