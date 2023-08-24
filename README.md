[![Test](https://github.com/P0rt/discord-bot/actions/workflows/bot.yml/badge.svg)](https://github.com/P0rt/discord-bot/actions/workflows/bot.yml)

# Discord Bot
A simple Discord bot powered by Python. This bot is designed to interact with users by sending requests to an external API.
```
DISCORD-BOT/
│
├── .github/
│   └── workflows/
│       └── bot.yml
│
├── src/
│   └── bot/
│       └── __init__.py
│       └── bot.py
│
├── tests/
│   └── __init__.py
│   └── test_bot.py
│
├── .gitignore
├── README.md
└── requirements.txt
```
## Features

- Send messages to an external API and retrieve responses.
- Built with `discord.py` library.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- A Discord account.
- A Heroku account something else.
- Python 3.9+ installed.

## Installation & Setup
```bash
git clone https://github.com/yourusername/discord-bot.git
```  
```bash
cd discord-bot  
```

**Set Up a Virtual Environment**:
You need add your token from Discord to GitHub Secret or in global env in your local machine  

**Environment Variables**:
Create a .env file in the root directory and add your Discord bot token:  
`DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN`  
  
**Install Dependencies**:
```bash
pip install -r requirements.txt
```
  
**Running Locally**:
```bash
python src/bot/bot.py
```

**Deploying to Heroku**

Login to Heroku and create a new app.  
Connect your GitHub repository to the app.  
Set the DISCORD_TOKEN environment variable in the Heroku app settings.  
Deploy the bot.  
  
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

**License**
https://choosealicense.com/licenses/mit/
