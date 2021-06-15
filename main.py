# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import os
from time import process_time
import discord
import sys
from dotenv import load_dotenv
from pyboy import PyBoy, WindowEvent  # isort:skip

adminID = "settoyourdiscordID"  # adminID for performing admin commands for restarting the bot, checking uptime, etc

# grabs the required SDL2.dll for pyboy to run
app_dir = os.path.dirname(os.path.realpath(__file__))
sdl2_dll_path = os.path.join(app_dir, "sdl2_dll")
os.environ["C:/SDL2/SDL2-2.0.10/lib/x64"] = sdl2_dll_path

# this bodge allows for a non-hardcoded way to find the screenshots folder
absolutepath = os.path.abspath(__file__)
fileDirectory = os.path.dirname(absolutepath)
parentDirectory = os.path.dirname(fileDirectory)
botPath = os.path.join(parentDirectory, 'DiscordPlaysPokemonBot')
screenshotsPath = os.path.join(botPath, 'screenshots')

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()
# Loads the .env file that resides on the same level as the script.
load_dotenv('key.env')
# Grab the API token from the .env file.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
print(os.getenv('DISCORD_TOKEN'))

# Check if the ROM is given through argv
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print("Usage: python main.py [ROM file]")
    exit(1)
quiet = False
pyboy = PyBoy(filename)
# pyboy: PyBoy = PyBoy(filename,window_type="headless" if quiet else "SDL2", window_scale=3, debug=False, game_wrapper=False)
pyboy.set_emulation_speed(4)
print(pyboy.cartridge_title())


# grabs the newest file from a given path
def newest(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)


# grabs the oldest file from a given path
def oldest(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return min(paths, key=os.path.getctime)


# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in bot.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print("DiscordPlaysPokemon is in " + str(guild_count) + " guilds.")


@bot.event
async def on_message(message):
    async def take_and_send_image():
        # This weird block of code takes and sends the screen updates, but for some reason I had to do it twice to get it to work reliably. Otherwise, works good.
        for _ in range(2):
            pyboy.tick()
            pyboy.send_input(WindowEvent.SCREENSHOT_RECORD)
            pyboy.send_input(WindowEvent.STATE_SAVE)
        await message.channel.send(file=discord.File(newest(screenshotsPath)))
        os.remove(oldest(screenshotsPath))
        os.remove(oldest(screenshotsPath))

    # below here is a lot of repeated code for handling movement/buttons, and some other stuff
    buttonPressed = False
    frameRuntime = 120
    if message.content == ">A":
        await message.channel.send("Pressing A")
        for frame in range(frameRuntime):
            pyboy.tick()
            if not buttonPressed:
                pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
                pyboy.tick()
                pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
                buttonPressed = True
            if frame == frameRuntime - 1:
                await take_and_send_image()

    if message.content == ">B":
        await message.channel.send("Pressing B")
        for frame in range(frameRuntime):
            pyboy.tick()
            if not buttonPressed:
                pyboy.send_input(WindowEvent.PRESS_BUTTON_B)
                pyboy.tick()
                pyboy.send_input(WindowEvent.RELEASE_BUTTON_B)
                buttonPressed = True
            if frame == frameRuntime - 1:
                await take_and_send_image()

    if message.content == ">UP":
        await message.channel.send("Pressing UP")
        for frame in range(frameRuntime):
            pyboy.tick()
            if not buttonPressed:
                pyboy.send_input(WindowEvent.PRESS_ARROW_UP)
                for _ in range(8):
                    pyboy.tick()
                pyboy.send_input(WindowEvent.RELEASE_ARROW_UP)
                buttonPressed = True
            if frame == frameRuntime - 1:
                await take_and_send_image()

    if message.content == ">DOWN":
        await message.channel.send("Pressing DOWN")
        for frame in range(frameRuntime):
            pyboy.tick()
            if not buttonPressed:
                pyboy.send_input(WindowEvent.PRESS_ARROW_DOWN)
                for _ in range(8):
                    pyboy.tick()
                pyboy.send_input(WindowEvent.RELEASE_ARROW_DOWN)
                buttonPressed = True
            if frame == frameRuntime - 1:
                await take_and_send_image()

    if message.content == ">LEFT":
        await message.channel.send("Pressing LEFT")
        for frame in range(frameRuntime):
            pyboy.tick()
            if not buttonPressed:
                pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)
                for _ in range(8):
                    pyboy.tick()
                pyboy.send_input(WindowEvent.RELEASE_ARROW_LEFT)
                buttonPressed = True
            if frame == frameRuntime - 1:
                await take_and_send_image()

    if message.content == ">RIGHT":
        await message.channel.send("Pressing RIGHT")
        for frame in range(frameRuntime):
            pyboy.tick()
            if not buttonPressed:
                pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
                for _ in range(8):
                    pyboy.tick()
                pyboy.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
                buttonPressed = True
            if frame == frameRuntime - 1:
                await take_and_send_image()

    if message.content == ">START":
        await message.channel.send("Pressing START")
        for frame in range(frameRuntime):
            pyboy.tick()
            if not buttonPressed:
                pyboy.send_input(WindowEvent.PRESS_BUTTON_START)
                pyboy.tick()
                pyboy.send_input(WindowEvent.RELEASE_BUTTON_START)
                buttonPressed = True
            if frame == frameRuntime - 1:
                await take_and_send_image()

    if message.content == ">SHOWSCREEN":
        await take_and_send_image()

    if message.content == ">HELP":
        await message.channel.send("Do >and then either UP, DOWN, LEFT, RIGHT, A, B ")

    # quick admin commands for debugging or restarting the bot
    if message.content == ">ADMIN MODE" and (message.author == adminID):
        print(str(message.author.id) + "accessed admin mode")
        cmd = input("Enter a command")
        if cmd == "LOADSTATE":
            pyboy.send_input(WindowEvent.STATE_LOAD)
        elif cmd == "UPTIME":
            print(process_time())
        elif cmd == "SETSPEED":
            val = input("Enter a speed as an integer multiple:")
            pyboy.set_emulation_speed(int(val))


bot.run(DISCORD_TOKEN)

# CREDITS
# Heavily edited starter code credited to Eric Chi's sample bot
# https://github.com/ericjaychi/sample-discord-bot
# The PyBoy discord, especially krs013, for tons of help debugging
# Newest and oldest files functions were partially skidded from stackoverflow user glglgl
