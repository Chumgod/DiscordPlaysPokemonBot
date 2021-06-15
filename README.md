# DiscordPlaysPokemonBot
Discord bot that plays gameboy games via discord commands, initially intended to play pokemon, but works with any gameboy ROM. 

Requirements:

SDL2
https://www.libsdl.org/download-2.0.php

Package Requirements:

discord~=1.0.1

python-dotenv~=0.15.0

pyboy~=1.3.0

pip~=20.3.3

setuptools~=51.1.2

Cython~=0.29.21

Usage instructions:
Change the DISCORD_TOKEN variable in key.env to your bot token
Change the adminID variable in main.py to your discord ID
Change the command-line arguments in your IDE(or input them manually) to your rom location. Example "C:\PokemonRed\PokemonRed.gb"
