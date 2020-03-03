from secret_santa_bot import *


def main():
    client = discord.Client()

    @client.event
    async def on_message(message):
        guild = client.get_guild(id=)
        # Remove whitespace from the message.
        command = message.content.strip()

        # If the message author isn't the bot.
        if message.author != client.user:
            # Add the 'Santa' role to the server if it has not already been done using default parameters/permissions.
            # Give the 'Santa' role to the user that used the '.add santa' command.
            if command == '.add santa':
                role_names = [role.name for role in guild.roles]
                if 'Santa' not in role_names:
                    await guild.create_role(name='Santa')

                def get_role(roles, wanted_role):
                    for role in roles:
                        if role.name == wanted_role:
                            return role

                await message.author.add_roles(get_role(guild.roles, 'Santa'))
                await message.channel.send('Added ' + str(message.author) + ' to the Santa List.')

            # Bot messages the list of members with the 'Santa' role.
            if command == '.santa list':
                await message.channel.send('\n'.join([member.name for member in guild.members for role in member.roles
                                                      if role.name == 'Santa']))

            # Begin secret Santa.
            # Every participant receives the welcome message for the start of the event and the name of their giftee.
            if command == '.santa bot activate':
                santas = [member for member in guild.members for role in member.roles if role.name == 'Santa']
                # Randomize and pair up participants.
                santas = pairup(santas)
                for pair in santas:
                    await pair['giftee'].send(santa_message)
                    time.sleep(10)
                    # Cover giftee's name with spoiler tags.
                    await pair['gifter'].send('You are ||' + pair['giftee'].name + "'s|| Santa.")

            # Users tell the bot they have sent their gift.
            # A plaintext file is kept with the names of the users who have gifted their giftee.
            # Santa Bot also messages the list of Santas that have completed their job each time '.gifted' is called.
            if command == '.gifted':
                retired_santas = os.path.join(os.path.dirname(__file__), 'retired_santas.txt')
                with open(retired_santas, 'r+') as retiree_file:
                    if str(message.author).strip() in retiree_file.read().strip():
                        await message.channel.send('You have already been retired.')
                    else:
                        retiree_file.write('\n' + str(message.author))
                        await message.channel.send('You are hereby retired from your role as santa, %s' %
                                                   str(message.author)[:-5])
                    await message.channel.send('Now, the following Santas have finished their job:\n' +
                                               retiree_file.read())

            # Test command to make sure Santa Bot is hooked up correctly.
            if command == '.test':
                await message.channel.send("Hello Pepe!")

            # Help command to explain all available commands.
            if command == '.help':
                pass

    client.run("")


if __name__ == "__main__":
    main()

