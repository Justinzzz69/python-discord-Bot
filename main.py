import discord
import random

from past.builtins import raw_input

eingabe=input("Gebe dein Bot Token ein:")


class MyClient(discord.Client):
    async def on_ready(self):
        print('Eingeloggt als', self.user)

    async def on_message(self, message):
        # verhindert auf sich selber zu antworten
        if message.author == self.user:
            return

        if message.content.startswith("!ping"):
            await message.channel.send("pong!")

        if message.content.startswith("!würfel"):
            number = random.randint(1, 6)
            await message.channel.send(f"Du hast die Zahl {number} gewürfelt")

        if message.content.startswith("!münze"):
            number = random.randint(1, 2)
            if number == 1:await message.channel.send("https://zufallsgenerator.org/kopf-oder-zahl/euro-head.png")
            else:await message.channel.send("https://zufallsgenerator.org/kopf-oder-zahl/euro-tail.png")

        if message.content.startswith("!schlong"):
            #der Bot erwähnt den user {message.author.mention}
            await message.channel.send(f"{message.author.mention} hat so ein großen Schlong")
            await message.channel.send(f"https://media.tenor.com/qTeM434Ja3AAAAAC/giga-chad-chad.gif")
        if message.content.startswith("!cmd"):
            await message.channel.send("meine Commands sind, **!ping, !würfel, !münze, !cmd, !schlong, !hi**")
            #Der Bot schreibt eine DM
        if message.content.startswith("!hi"):
            await message.author.send("Immer Fresh bleiben du Nudel")
            await message.author.send("https://media.tenor.com/KlqGv765bt4AAAAi/feet-dude.gif")
            #der Bot antwortet auf eine Nachricht wenn das Wort im kontext geschrieben wird
        if "hallo" in message.content.lower():
            await message.channel.send("na du hund")


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(eingabe)
raw_input()
