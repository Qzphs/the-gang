Discord bot for playing [The Gang](https://boardgamegeek.com/boardgame/411567/the-gang).
This bot manages custom challenges.

# Setup

You need 3 things: this code, your own Discord bot, and discord.py. Follow the
instructions below (in order) to set up each of them.


## Source code

On the GitHub page, click the green **Code** button, then click
**Download ZIP**. Unzip this on your computer (this is the source code folder
I refer to later on).


## Discord bot

Go to the [Discord Developer Portal](https://discord.com/developers/applications).
There's a couple things you need to do, which I've roughly grouped into 2 steps.


### Create new bot

Click **New Application** in the top right. Name your bot and continue.

Go to the **Bot** tab and copy the token. In the source code folder, create a
new file called **token.txt** and paste the token you copied in there.

Also in the **Bot** tab, turn off **Public Bot** and turn on all intents.

Your token is your bot's password. Don't show it to anyone.


### Add bot to server

Go to the **OAuth2** tab and scroll down to the giant panel of checkboxes. Tick
**bot**.

This will reveal another giant panel of checkboxes. In that one, tick
**Send Messages**, **Read Message History**, and **Use Slash Commands**.

Copy the **Generated URL** at the bottom and paste it into your browser. This
should open a prompt in either Discord or the browser asking you for permission
to add your bot. Choose which server you want to add the bot to.


## discord.py

You will need [Python](https://www.python.org/downloads/) installed.

To install discord.py, you need to first download the source code (instructions
above). Open a terminal at the source code folder. There are 3 commands you
need to run.


### Create a virtual environment

You only need to do this once. Skip this step if you already have a **venv**
folder in the source code folder.

Windows:
```
py -m venv venv
```

macOS:
```
python3 -m venv venv
```


### Activate the virtual environment

Windows:

```
venv\Scripts\activate.bat
```

macOS:

```
source venv/bin/activate
```


### Install discord.py

Windows:
```
py -m pip install discord.py
```

macOS:
```
python3 -m pip install discord.py
```


## Challenges

Write each challenge on its own line in **challenges.txt**. Challenges need an
author and a description, separated by colon (`:`).

This is an example of what a valid file looks like:

```
base: skip round 2
qzphs: 5 bid limit
```


# Running the bot

Open a terminal at the source code folder. There are 2 commands you need to
run.


### Activate the virtual environment

Windows:
```
venv\Scripts\activate.bat
```

macOS:
```
source venv/bin/activate
```


### Start the bot

Windows:
```
py bot.py
```

macOS:
```
python3 bot.py
```


### Stop the bot

Use the **/quit** command on Discord.

If that's not working for some reason, you can also force quit the bot on your
side by typing Ctrl-C into the terminal (same for both Windows and macOS).


### Start the bot (and sync commands)

You might need to sync bot commands if it's your first time running the bot.
Use this command instead of the normal run command if there's no error message
but none of the bot's commands show up on Discord.

Windows:
```
py bot.py --sync
```

macOS:
```
python3 bot.py --sync
```
