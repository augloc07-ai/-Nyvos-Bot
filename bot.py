import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")
WELCOME_CHANNEL_ID = int(os.getenv("WELCOME_CHANNEL_ID"))

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"Nyvos Bot online: {bot.user}")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)

    if channel is None:
        print("Canale di benvenuto non trovato.")
        return

    await channel.send(
        f"💜 Benvenuto nei **Nyvos**, {member.mention}! 🎮\n\n"
        "Questo è il nostro spazio per stare insieme anche fuori dalle live.\n"
        "Parla di gaming e di tanto altro, partecipa alla chat, "
        "condividi i tuoi clip e conosci gli altri Nyvos.\n\n"
        "Grazie di essere qui e buona permanenza nella community! 💜"
    )


if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN non configurato.")

bot.run(TOKEN)
