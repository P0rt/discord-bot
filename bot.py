import discord
from discord.ext import commands
import requests
import os

TOKEN = os.environ.get('DISCORD_TOKEN')
API_BASE_URL = 'http://144.76.41.116:1958/query/'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def chat(ctx, *, message):
    async with ctx.typing():
        response = send_to_api(message)
    await ctx.send(response)


def send_to_api(message):
    try:
        # Кодируем сообщение для использования в URL
        encoded_message = requests.utils.quote(message)
        full_url = f"{API_BASE_URL}?q={encoded_message}"

        response = requests.get(full_url)
        response.raise_for_status()
        
        response_data = response.json()
        content = response_data.get('choices', [{}])[0].get('message', {}).get('content')
        
        if not content:
            return f"Unexpected API response: {response_data}"
        
        return content
    except requests.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as e:
        return f"Error: {e}"

bot.run(TOKEN)
