import discord
from discord.ext import commands
from translator import detect_language, transliterate
import re

# Вообще тут должен dotenv но мне лень, сами сделаете
TOKEN = 'YOUR_BOT_TOKEN'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

def contains_link(text):

    # Простая проверка на наличие ссылок
    return re.search(r'http[s]?://', text) is not None

@bot.command(name='translate')
async def translate(ctx):
    if ctx.message.reference is None:
        await ctx.send("Пожалуйста, ответьте на сообщение, которое нужно перевести.")
        return

    # Получаем сообщение, на которое был дан ответ
    referenced_message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
    text = referenced_message.content

    if contains_link(text):
        await ctx.send("Сообщение содержит ссылку и не может быть переведено.")
        return

    # Удаляем эмодзи в формате :emoji:
    text_without_emojis = re.sub(r':[a-zA-Z0-9_]+:', '', text)

    language = detect_language(text_without_emojis)
    output_text = transliterate(text_without_emojis, language)
    await ctx.send(output_text)

bot.run(TOKEN)
