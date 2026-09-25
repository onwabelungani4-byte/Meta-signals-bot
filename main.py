from flask import Flask
from threading import Thread
import os
import discord
from discord.ext import commands

# --- Keep Render Alive ---
app = Flask('')
@app.route('/')
def home():
    return "Bot Online"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

Thread(target=run).start()

# --- Discord Bot ---
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Online as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} commands")
    except Exception as e:
        print(f"Sync error: {e}")

@bot.tree.command(name="signal", description="Get latest Meta forex signal")
async def signal(interaction: discord.Interaction):
    embed = discord.Embed(
        title="📈 META SIGNALS - XAUUSD",
        description="**High Probability Setup**",
        color=0x00ff00
    )
    embed.add_field(name="📊 Action", value="**BUY**", inline=True)
    embed.add_field(name="💰 Entry", value="2680.5", inline=True)
    embed.add_field(name="🎯 Take Profit", value="2700.0", inline=True)
    embed.add_field(name="🛑 Stop Loss", value="2670.0", inline=True)
    embed.add_field(name="⏰ Timeframe", value="H1", inline=True)
    embed.set_footer(text="Meta Signals Bot • Not financial advice")
    
    await interaction.response.send_message(embed=embed)

# --- RUN WITH BOTH TOKEN NAMES ---
TOKEN = os.getenv("TOKEN") or os.getenv("DISCORD_TOKEN")

if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ ERROR: No TOKEN found in Environment!")
