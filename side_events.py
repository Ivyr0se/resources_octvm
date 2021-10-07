# Do it again!
botlog = 890596163118596117
botlog_spam = 894969006581248030

@bot.event
async def on_member_join(user: discord.Member):
    perm_on_member_join = await check_db("perm_on_member_join")
    content_on_member_join = await check_db("on_member_join_content")
    perm_on_member_join_add = await check_db("perm_on_member_join_add")
    if perm_on_member_join == "True":
        db_on_member_join_ch = bot.get_channel(890596290168258630)
        message = await db_on_member_join_ch.fetch_message(890597077359419412)
        channel = bot.get_channel(int(message.content))
        await channel.send(user.mention + ", " + str(content_on_member_join))
    else:
        return


@bot.event
async def on_message_edit(before, after):
    try:
        if before.content != after.content:
            gld = before.guild.id
            ch_int = await get_ch_id("audit", gld)
            ch = bot.get_channel(ch_int)

            embedVar = discord.Embed(title="Message Edited in " + "#" + str(before.channel), color=0x2C5ED1)
            embedVar.add_field(name=str(before.author), value="**Before:** " + str(before.content), inline=False)
            embedVar.add_field(name="** **", value="**After:** " + str(after.content), inline=False)
            await ch.send(embed=embedVar)
    except AttributeError:
        pass
    except Exception as e:
        botlog_func = bot.get_channel(botlog)
        embedVar = discord.Embed(title="Error;", color=0x2C5ED1)
        embedVar.add_field(name="** **", value=str(e), inline=False)
        embed = await botlog_func.send(embed=embedVar)





@bot.event
async def on_member_update(before, after):
    try:
        gld = before.guild.id
        ch_int = await get_ch_id("audit", gld)
        ch = bot.get_channel(ch_int)

        user = str(before.name) + "#" + str(before.discriminator)
        if before.nick != after.nick:
            embedVar = discord.Embed(title="Nickname Changed", color=0x2C5ED1)
            embedVar.add_field(name=user, value="**Before:** " + str(before.nick), inline=False)
            embedVar.add_field(name="** **", value="**After:** " + str(after.nick), inline=False)
            await ch.send(embed=embedVar)

        if before.name != after.name:
            embedVar = discord.Embed(title="Username Changed", color=0x2C5ED1)
            embedVar.add_field(name=user, value="**Before:** " + str(before.name), inline=False)
            embedVar.add_field(name="** **", value="**After:** " + str(after.name), inline=False)
            await ch.send(embed=embedVar)

        if before.avatar != after.avatar:
            embedVar = discord.Embed(title="Avatar Changed", color=0x2C5ED1)
            embedVar.add_field(name=user, value="** **", inline=False)
            await ch.send(embed=embedVar)
    except AttributeError:
        pass
    except Exception as e:
        botlog_func = bot.get_channel(botlog)
        embedVar = discord.Embed(title="Error;", color=0x2C5ED1)
        embedVar.add_field(name="** **", value=str(e), inline=False)
        embed = await botlog_func.send(embed=embedVar)



@bot.event
async def on_message_delete(message):
    try:
        gld = message.guild.id
        ch_int = await get_ch_id("audit", gld)
        ch = bot.get_channel(ch_int)

        user = message.author
        embedVar = discord.Embed(title="Message Deleted in " + "#" + str(message.channel), color=0x2C5ED1)
        embedVar.add_field(name=user, value="**Content:** " + str(message.content), inline=False)
        await ch.send(embed=embedVar)
    except AttributeError:
        pass
    except Exception as e:
        botlog_func = bot.get_channel(botlog)
        embedVar = discord.Embed(title="Error;", color=0x2C5ED1)
        embedVar.add_field(name="** **", value=str(e), inline=False)
        embed = await botlog_func.send(embed=embedVar)


@bot.event
async def on_message(message):
    # Task Loop Ensurer
    result_inst = await check_db("track_instance")
    result_int = await check_db("track_interest")
    result_int = int(result_int)
    if result_inst == "True" and track_instance == False:
        global track_interest
        track_interest = int(result_int)
    if message.author.id == track_interest:
        page = await get_page("https://raw.githubusercontent.com/azrael28gmail/resources_octvm/main/track_log.txt")
        content = str(page) + "\n" + str(message.content) + " (" +  str(message.created_at) + "," + str(message.guild) + ")"
        await append_file("track_log.txt", "resources_octvm", content)
        log = bot.get_channel(botlog_spam); await log.send("Logged a new message: " + str(message.content))
    await bot.process_commands(message)

@bot.event
async def on_guild_join(guild):
  log = bot.get_channel(botlog_spam)
  await log.send("Joined: " + str(guild))

@bot.event
async def on_guild_remove(guild):
  log = bot.get_channel(botlog_spam)
  await log.send("Left: " + str(guild))

