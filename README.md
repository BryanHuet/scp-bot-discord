# SCP Discord Bot

## Introduction
This Discord bot is designed to detect when users talk about SCPs (Secure, Contain, Protect) within a Discord server and respond with the image and name of the mentioned SCP. SCPs are fictional anomalous objects, entities, and locations documented by the SCP Foundation, a fictional organization responsible for containing and researching them.

## Features
- **SCP Detection**: The bot scans messages in real-time to identify mentions of SCPs.
- **Information Retrieval**: Upon detecting an SCP mention, the bot retrieves the corresponding image and name.
- **Interactive Response**: Users receive an immediate response with the SCP's image and name.

## Installation
1. Clone this repository to your local machine.
3. Create a Discord bot application and obtain its token from the [Discord Developer Portal](https://discord.com/developers/applications).
4. Create a `.env` file in the root directory and add your bot token:
    ```
    DISCORD_TOKEN=your_bot_token_here
    ```
5. Run the bot using `start.sh`.

## Dependencies
- [discord.py](https://discordpy.readthedocs.io/en/stable/): Used for interacting with the Discord API.
  
## Usage
- Invite the bot to your Discord server.
- Mention any SCP within a message (e.g., "SCP-173 is creepy!").
- The bot will respond with the image and name of the mentioned SCP.


## Sources
- **SCP Database:** http://fondationscp.wikidot.com/
