import discord
import asyncio
from lb_functions import help, stats, format, types, types_print, dual_types, mono, get_token
from lb_move_functions import move_info, move_print


client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    # Info
    if message.content.startswith('*info'):
        m = '```Hello, I am Lillie\n' \
            + 'Type *help for a list of commands```'
        await client.send_message(message.channel, m)

    # Pic
    elif message.content.startswith('*pic'):
        args = message.content.upper().split()
        if len(args) != 2:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')
        else:

            if args[1].isnumeric():
                info = stats(1, args[1])
            else:
                info = stats(2, args[1])

            m = info[0]

            await client.send_message(message.channel, m)

    # Stats
    elif message.content.startswith('*stats'):
        args = message.content.upper().split()
        if len(args) != 2:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')
        else:

            if args[1].isnumeric():
                info = stats(1, args[1])
            else:
                info = stats(2, args[1])

            if info != -1:
                m = format(info)
                await client.send_message(message.channel, info[0])
                await client.send_message(message.channel, m)

    # Stats
    elif message.content.startswith('*move'):
        args = message.content.upper().split()
        if len(args) < 2:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')
        elif len(args) == 3:

            move_name = args[1] + ' ' + args[2]
            info = move_info(move_name)

            if info != -1:
                m = move_print(info)
                await client.send_message(message.channel, m)
        else:
            info = move_info(args[1])

            if info != -1:
                m = move_print(info)
                await client.send_message(message.channel, m)

    # Help
    elif message.content.startswith('*help'):
        await client.send_message(message.channel, help())

    # Type
    elif message.content.startswith('*type'):
        args = message.content.upper().split()
        if len(args) != 2:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')
        else:
            type_list = types(args[1])
            if len(type_list) != 0:
                await client.send_message(message.channel, types_print(type_list))

    # types
    elif message.content.startswith('*dual'):
        args = message.content.upper().split()
        if len(args) != 3:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')
        else:
            type_list = dual_types(args[1], args[2])
            if len(type_list) != 0:
                await client.send_message(message.channel, types_print(type_list))

    # types
    elif message.content.startswith('*mono'):
        args = message.content.upper().split()
        if len(args) != 2:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')
        else:
            type_list = mono(args[1])
            if len(type_list) != 0:
                await client.send_message(message.channel, types_print(type_list))

bot_token = get_token()

client.run(bot_token)
