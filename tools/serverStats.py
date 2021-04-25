from discord import Status, Embed, Color

async def serverstats(ctx):

    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    membersCount = str(ctx.guild.member_count)

    botsCount = 0
    usersOnline = 0
    botsOnline = 0
    onlineStatus = [
        Status.online,
        Status.idle,
        Status.dnd
    ]

    for member in ctx.guild.members:
        if member.bot:
            botsCount += 1

        if member.status in onlineStatus:
            if member.bot:
                botsOnline += 1
            else:
                usersOnline += 1

    icon = str(ctx.guild.icon_url)

    embed = Embed(
        title=name + " Server Information",
        description=description,
        color=Color.blue()
    )

    usersCount = int(membersCount) - botsCount
    botsOffline = botsCount - botsOnline
    usersOffline =usersCount - usersOnline

    usersCount = str(usersCount)
    botsOffline = str(botsOffline)
    usersOffline = str(usersOffline)
    botsCount = str(botsCount)
    botsOnline = str(botsOnline)
    usersOnline = str(usersOnline)

    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    
    embed.add_field(name="Users", value=usersCount, inline=True)
    embed.add_field(name="Users Online", value=usersOnline, inline=True)
    embed.add_field(name="Users Offline", value=usersOffline, inline=True)

    embed.add_field(name="Bots", value=botsCount, inline=True)
    embed.add_field(name="Bots Online", value=botsOnline, inline=True)
    embed.add_field(name="Bots Offline", value=botsOffline, inline=True)

    embed.add_field(name="Total Members", value=membersCount, inline=True)

    await ctx.send(embed=embed)
    return