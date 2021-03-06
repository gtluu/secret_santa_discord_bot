# Old Pepe
import os
import discord
import random
from collections import deque


def pairup(people):
    random.shuffle(people)
    partners = deque(people)
    partners.rotate()
    return (zip(people, partners))


if __name__ == "__main__":

    client = discord.Client()

    santa_message = "Thank you for participating in PCS Secret Santa 2019. A couple things to note: feel free to give someone something that is on their Steam wishlist, or something that they've been wanting from elsewhere, at whatever price is affordable, and make sure to keep your own wishlist updated (don't just have super expensive games you greedy boi)."


    @client.event
    async def on_message(message):
        guild = client.get_guild(id=)
        if message.author != client.user:
            if message.content == ".santas":
                for member in guild.members:
                    for role in member.roles:
                        if role.name == "Santa":
                            print(member)
                            await message.channel.send(member)
            if message.content == ".santa bot activate":
                people = []
                for member in guild.members:
                    for role in member.roles:
                        if role.name == "Santa":
                            people.append(member)
                santas = pairup(people)
                for pair in santas:
                    print("Santa: " + pair[0].name)
                    print("Receiver: " + pair[1].name)
                    print('\n')
                    await pair[0].send(santa_message)
                    await pair[0].send("You are " + str(pair[1]) + "'s santa.")
            if message.content == ".gifted":
                retired_santas_txt = os.path.dirname(os.path.abspath(__file__)) + "\giftedbois.txt"
                with open(retired_santas_txt, 'r+') as file_obj:
                    if str(message.author).strip() in file_obj.read().strip():
                        await message.channel.send("You've already been added to the list, bucko.")

                    elif str(message.author) not in file_obj.read().strip():
                        await message.channel.send(
                            "You are hereby retired from your role as Santa, %s" % str(message.author)[:-5])
                        file_obj.write("\n" + str(message.author))
                await message.channel.send("Now, The following Santas have finished their job:\n")
                with open(retired_santas_txt, 'r') as file_obj:
                    for line in file_obj:
                        await message.channel.send(line + "\n")
            if message.content == ".test":
                print("Hello Pepe!")


    client.run("")
   
