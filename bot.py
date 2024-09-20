import discord
from discord.ext import commands

# İntentleri ayarlıyoruz
intents = discord.Intents.default()
intents.message_content = True  # Mesaj içeriklerini dinleyebilmek için bu intent'i açıyoruz.

# Botu oluşturuyoruz ve intents'i geçiyoruz
bot = commands.Bot(command_prefix="!", intents=intents)

# Basit bir komut örneği
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Görev ekleme komutu örneği
@bot.command()
async def add_task(ctx, *, description):
    await ctx.send(f"Görev eklendi: {description}")

# Botu başlatıyoruz
bot.run("token")
