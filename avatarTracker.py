from flask import Flask, jsonify, request
import discord
import asyncio
import os
from threading import Thread
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

USER_ID = 1181256087081603116 # replace with the user id whose avatar your want to fetch.
DISCORD_BOT_TOKEN = ''
API_KEY = 'ilovemilfgirlsfr' # you can edit of your own choice!

avatar_url = None

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        await self.avatar_update_loop()

    async def avatar_update_loop(self):
        while True:
            await self.update_avatar()
            await asyncio.sleep(10) # checks every 10s

    async def update_avatar(self):
        global avatar_url
        user = await self.fetch_user(USER_ID)
        new_avatar_url = str(user.avatar.url) if user.avatar else None
        if new_avatar_url != avatar_url:
            avatar_url = new_avatar_url
            print(f"[ ! ] :- Avatar updated: {avatar_url}")

intents = discord.Intents.default()
client = MyClient(intents=intents)

@app.route('/api/avatar')
def get_avatar():
    api_key = request.args.get('api_key')
    if api_key != API_KEY:
        return jsonify({'error': 'Invalid API key'}), 403
    return jsonify({'avatar_url': avatar_url})

def run_discord_bot():
    asyncio.run(client.start(DISCORD_BOT_TOKEN))

if __name__ == '__main__':
    Thread(target=run_discord_bot).start()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000))) # change it as your desired port on which your host runs. default 5000
