# Discord Avatar Tracker API

This project provides a Flask-based API that tracks and serves the current avatar URL of a specific Discord user. It combines a Discord bot to fetch real-time avatar updates with a web server to make this information accessible via HTTP requests.

## Features
- Real-time tracking of a Discord user's avatar changes
- RESTful API endpoint to retrieve the current avatar URL
- Discord bot integration using discord.py
- Flask web server with CORS support
- Simple API key authentication for secure access

## Setup
1. Clone this repository to your local machine or server.
2. Install the required dependencies:
3. Edit the following variables in the script:
- `USER_ID`: Replace with the Discord user ID you want to track
- `DISCORD_BOT_TOKEN`: Add your Discord bot token
- `API_KEY`: Set your desired API key for authentication

## Usage
1. Run the script:
2. The Discord bot will start and begin tracking the specified user's avatar.
3. The Flask server will start, by default on `http://0.0.0.0:5000`
4. To get the current avatar URL, make a GET request to:

## API Endpoint
- **URL**: `/api/avatar`
- **Method**: GET
- **URL Params**: 
- Required: `api_key=[string]`
- **Success Response**:
- Code: 200
- Content: `{ "avatar_url" : "https://cdn.discordapp.com/avatars/..." }`
- **Error Response**:
- Code: 403 FORBIDDEN
- Content: `{ "error" : "Invalid API key" }`

## Customization Points
1. `USER_ID`: Set this to the Discord user ID whose avatar you want to track.
2. `DISCORD_BOT_TOKEN`: Replace with your Discord bot's token.
3. `API_KEY`: Change this to your desired API key for authentication.
4. Port number: By default, the server runs on port 5000. You can change this by modifying the `PORT` environment variable or the default value in the `app.run()` call.

## Note
Remember to keep your Discord bot token and API key secure. Never share them publicly or commit them to version control.
