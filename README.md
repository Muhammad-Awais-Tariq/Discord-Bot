# Discord Bot

A simple Discord bot made for learning and testing purpose only.  
This project is **not a production-ready bot** and is meant to demonstrate basic Discord bot commands, event handling, role management, DMs, polls, and simple moderation.

## Features
- Welcomes new members with a private message
- Detects a restricted word and deletes the message
- Sends a greeting command
- Assigns and removes a specific role
- Sends direct messages to the user
- Creates simple poll messages with reactions
- Replies to users
- Restricts a command to members with a specific role
- Logs bot activity to a file

## Commands
- `!hello` — Sends a greeting
- `!assign` — Assigns the test role to the user
- `!remove` — Removes the test role from the user
- `!dm <message>` — Sends the user a direct message containing their text
- `!poll <question>` — Creates a poll embed with reaction options
- `!reply` — Bot replies with a message
- `!special` — Works only for users who have the required role

## How It Works
- The bot listens for member join events and sends a welcome message privately
- It checks every message for a restricted word and deletes it if found
- It uses custom commands for interaction
- It checks roles before allowing access to certain commands
- It writes logs to `Discord.log`

## Technologies Used
- Python
- discord.py
- python-dotenv
- logging
- os

## Project Structure
```bash
project/
│── main.py
│── README.md
│── .gitignore
│── .python-version
│── pyproject.toml
│── uv.lock
```

## Notes
- This bot was created only for learning and testing
- It is not a complete or polished Discord bot
- The role name used in the code is currently set as a test role
- The moderation feature only checks one restricted word and is very basic
- Logging is enabled for debugging and learning purposes

## Author
Muhammad Awais Tariq

---
If you like this project, consider giving it a star on GitHub!