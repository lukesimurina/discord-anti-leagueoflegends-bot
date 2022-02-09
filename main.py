from multiprocessing.connection import Client
import os
import discord

intents = discord.Intents.all()
intents.members = True

# Import TOKEN from .env using dotenv
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

# Create the client
client = discord.Client(intents=intents)

# Create client on ready
@client.event
async def on_ready():
    print("Logged in as", client.user)
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name="for losers..."
        )
    )


@client.event
async def on_member_update(before, after):
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=random.choice(status)))

    if after.activity != None:
        if len(after.activities) > 0:
            games = []
            for i in after.activities:
                games.append(i.name.lower())
            if "league of legends" in games:
                games = []
                channel = client.get_channel(940888883040751637)
                embed = discord.Embed(
                    title="LOSER DETECTED",
                    description="%s opened League of Legends" % after.mention,
                    color=0xFF0000,
                )
                embed.set_thumbnail(url=after.avatar_url)
                await channel.send(embed=embed)


client.run(TOKEN)
