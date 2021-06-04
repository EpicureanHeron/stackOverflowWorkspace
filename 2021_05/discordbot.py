# Command to know how much people are in general
@bot.command(name='presencas')
@commands.has_role(admin_id)
async def on_message(ctx):
    await ctx.send('Presenças no servidor no dia: ' + str(datetime.now().date()) + ' às ' + time.strftime(r"%H:%M") + 'H')
    with open('presencas_' + str(datetime.now().date()) + '.csv', 'w', newline='') as file:

        writer = csv.writer(file, delimiter=':', quoting=csv.QUOTE_NONE)
        writer.writerow(['Nome, tag, timestamp'])

        for user in ctx.guild.members:
            writer = csv.writer(file, delimiter='"', quoting=csv.QUOTE_NONE)
            if user.status != discord.Status.offline:
                writer.writerow([user.name + ', ' + '#'+user.discriminator + ', ' +str(datetime.now().date()) + ' ' + time.strftime(r"%H:%M") + 'H'])

    await ctx.send(file=discord.File(r'presencas_' + str(datetime.now().date()) + '.csv'))


#Command to know how much people are a specific channel
@bot.command()
@commands.has_role(admin_id)
async def presencascanal(ctx, canal):

    channel = bot.get_channel(int(canal))  # Canal de onde a lista vem

    members = channel.members  # Encontra os membros que estão no canal

    await ctx.send('Presenças no canal ' + channel.name + ' no dia ' + str(datetime.now().date()) + ' às ' + time.strftime(r"%H:%M") + 'H')
    with open('presencas_canal_' + channel.name + '_' + str(datetime.now().date()) + '.csv', 'w', newline='') as file:

        writer = csv.writer(file, delimiter=':', quoting=csv.QUOTE_NONE)
        writer.writerow(['Nome, tag, timestamp'])

        for user in members:
            writer = csv.writer(file, delimiter='"', quoting=csv.QUOTE_NONE)
            if user.status != discord.Status.offline:
                writer.writerow([user.name + ', ' + '#'+user.discriminator + ', ' +str(datetime.now().date()) + ' ' + time.strftime(r"%H:%M") + 'H'])

    await ctx.send(file=discord.File(r'presencas_canal_' + channel.name + '_' + str(datetime.now().date()) + '.csv'))