import discord
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='!')

# Join a voice channel
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    
    if voice_client is not None:
        await voice_client.move_to(channel)
    else:
        await channel.connect()

# Play music from a YouTube URL
@bot.command()
async def play(ctx, url):
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    
    if voice_client is None or not voice_client.is_connected():
        await ctx.send("I'm not connected to a voice channel. Use `!join` to bring me into a voice channel.")
        return
    
    # You'll need to set up a music playback library (e.g., ffmpeg, youtube-dl) to stream and play the music
    # Replace `your_playback_library.play(url)` with the appropriate code for your chosen library
    # For example, using FFmpeg:
    # voice_client.play(discord.FFmpegPCMAudio(url))
    
    await ctx.send("Playing music...")

# Leave the voice channel
@bot.command()
async def leave(ctx):
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    
    if voice_client is not None and voice_client.is_connected():
        await voice_client.disconnect()
        await ctx.send("I have left the voice channel.")
    else:
        await ctx.send("I'm not connected to a voice channel.")

# Run the bot
bot.run('YOUR_BOT_TOKEN')
