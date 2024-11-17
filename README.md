# Birthday-Bot
This MS Teams bot sends birthday greetings.

## Requirements

Install everything in the requirements.txt.
```
pip install -r requirements.txt
```
I recommend using a virtual environment with `python3-venv`.

## Configure and run

Create a .env file with your MS Teams Webhook.
```
WEBHOOK=<secret>
```

And then run it, to check for birthdays and send greetings to MS Teams.
```
python3 bday_bot.py
```

I recommend putting it in a crontab with `crontab -e`, e.g. to run it everyday at 3:14 AM.
```
14 3 * * * /path/to/python-venv/bin/python3 /path/to/Birthday-Bot/bday_bot.py > /path/to/log/output.log 2>&1
```
