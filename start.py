import disnake
from disnake.ext import commands
from translate import Translator
import function

#create bot

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!",intents=intents)

@bot.event
async def on_ready():
    print("Done!")

#command

@bot.slash_command(description="Показ погоды")
async def weather(ctx, city):
    translator1 = Translator(from_lang="en",to_lang="ru")

    city = function.weather(city)
    c = translator1.translate(city[0])
    t = city[1]
    w = translator1.translate(city[2])
    await ctx.send(f"Город: {c}\nТемпература: {t}\nПогода: {w}")


bot.run('TOKEN')