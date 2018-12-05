import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)

@client.event
async def on_message(message):
    if message.content.startswith('!deleteme'):
        msg = await client.send_message(message.channel, 'Сега ще изтрия себеси...')
        await client.delete_message(msg)

@client.event
async def on_message_delete(message):
    fmt = '{0.author.name} изтри своето съобщение:\n{0.content}'
    await client.send_message(message.channel, fmt.format(message))

client.run('NTE5ODE0MTMxODM5NDAxOTg0.Duk-cw.ydAaw4EZtLUKYfg708FMEiiYbvg')
