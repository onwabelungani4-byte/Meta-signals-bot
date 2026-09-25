import discord, os
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Online {bot.user}")
    await bot.tree.sync()

@bot.tree.command(name="signal", description="Send XAUUSD signal")
async def signal(interaction: discord.Interaction, pair: str, action: str, entry: str, sl: str, tp: str):
    embed = discord.Embed(title=f"{pair} SIGNAL", color=0x00ff00)
    embed.add_field(name="Action", value=action)
    embed.add_field(name="Entry", value=entry)
    embed.add_field(name="SL", value=sl)
    embed.add_field(name="TP", value=tp)
    await interaction.response.send_message(embed=embed)

bot.run(os.getenv("DISCORD_TOKEN"))
