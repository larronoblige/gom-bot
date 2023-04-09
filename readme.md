**Requirements**

* gspread
* discord.py
* asyncio

Go follow [these steps](https://docs.gspread.org/en/v5.7.2/oauth2.html#service-account) to be able to link it to your sheets. Only difference is to place your credentials.json in the same directory as the python files. Discord bot token gets put in bot.py.

---

This was coded on, and generally assumes you're following a spreadsheet format that looks like this:

| discord | quantity | cost | status |
|guy#0000 |         4|    18|paid    |

You can add/remove/modify columns as needed, but bare minimum it needs discord & status to run. It doesn't work if the headers are on the rows but column order doesn't matter.


**!contact [sheet] [message to send] [status] [worksheet (opt)]**
Sends a DM to all users, provided you're following the general spreadsheet format. You can use column header names as arguments, e.g.,

> Your total is ${cost}

Will replace {cost} with the appropriate value, like:

| name | cost |
| john | 4    |

Yields

> Your total is $4

Sheet - The nickname OR sheet id

Message - You can use any column header wrapped in {} as variables/placeholders. You will need to wrap the message in quotes

Status - What the bot is supposed to check for. Specifically it's matching status, so make it something like 'unpaid' or 'not dmed'

Worksheet - Optional, defaults to 'Sheet1'. Use this if your sheet isn't named that

**!paid [split] [username#0000]**

Used by claimers to denote they've paid. Updates the 'status' column to 'paid'. I suggest giving your claimer the exact command so they don't mess it up somehow, e.g., in your !contact [message] it could say:

> Once you've paid, copy and paste this command and send it to the bot:
> !paid (split nickname) {discord}

This uses nicknames, so you're not handing your sheet id over to claimers. Nicknames are stored in a dictionary in botfunctions.py, and are accessed with getNickname(nickname). e.g.,

```'pashas': 'euwoaubhjasdjmn_bwueouaouweuobahm',```

This is *not* meant to store many different nicknames, just a few that you're actively running splits for & are using the bot on. If you want to store a bunch of nicknames, make a json file.

**!q [message]**

Relays a message to the GOM. 

**!ping**

Obligatory & self explanatory.

**!dm [user#0000] [message]**

Sends a DM to the specified user. Is meant to have string variables passed into it, and doesn't accept multiple users. It's not really meant to be a frequently used command, but if for whatever reason you want to DM a user via. the bot you can.