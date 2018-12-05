import discord

client = discord.Client()

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Здр {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NTE5ODE0MTMxODM5NDAxOTg0.Duk-cw.ydAaw4EZtLUKYfg708FMEiiYbvg')
