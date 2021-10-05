async def change_db(ch_name, new):
                fetch_arg = ch_name
                db_func = discord.utils.get(bot.get_all_channels(), name=fetch_arg)
                channel_id = db_func.id
                db_user = bot.get_channel(channel_id)

                msg_info = discord.utils.get(await db_user.history(limit=100).flatten())
                msg = msg_info.content
                msg_id = msg_info.id
                msg_fetch = await db_user.fetch_message(msg_id)
                new_db = str(new)
                await msg_fetch.edit(content=new_db)

async def check_db(check: str):
                fetch_arg = check
                db_func = discord.utils.get(bot.get_all_channels(), name=fetch_arg)
                channel_id = db_func.id
                db_user = bot.get_channel(channel_id)

                msg_info = discord.utils.get(await db_user.history(limit=100).flatten())
                msg = msg_info.content
                msg_id = msg_info.id
                msg_fetch = await db_user.fetch_message(msg_id)
                return msg

async def get_ch_id(check, guild_id):
                guild = bot.get_guild(guild_id)
                db_func = discord.utils.get(guild.channels, name=check)
                channel_id = db_func.id
                return channel_id

async def get_user_roles(user):
    roles = []
    for role in user.roles:
        roles.append(str(role))
    return roles


async def check_list(lst, element):
    check = False
    for i in lst:
        if i == element:
            check = True
    return check

async def append_file(filename, reponame, content):
    filename = "/" + filename
    pure_filename = filename.replace("/", "")
    pure_filename = filename.replace(".txt", "")
    g = Github(GB_TOKEN)

    repo = g.get_user().get_repo(reponame)
    contents = repo.get_contents(filename)
    repo.update_file(contents.path, "None", content, contents.sha)


async def clear_file(filename, reponame):
    filename = "/" + filename
    g = Github(GB_TOKEN)

    repo = g.get_user().get_repo(reponame)
    contents = repo.get_contents(filename)
    repo.update_file(contents.path, "None", "None", contents.sha)

async def create_file(filename, reponame):
    g = Github(GB_TOKEN)

    repo = g.get_user().get_repo(reponame)
    repo.create_file(filename, "None", "None")



async def get_page(url):
    page = requests.get(url)
    return page.text

async def loop_ensurer(type):
  log = bot.get_channel(botlog)
  if type == "track":
    result_inst = await check_db("track_instance")
    result_int = await check_db("track_interest")
    result_int = int(result_int)
    await log.send("Loop Ensurer initiated, type: track")
    if result_inst == "True" and track_instance == False:
      global track_interest
      track_interest = int(result_int)
      await log.send("Finished Loop Ensurer, type: track")
  elif type == "stock":
    result_inst = await check_db("stock_instance")
    interest = await check_db("stock_interest")
    await log.send("Loop Ensurer initiated, type: stock")
    if result_inst == "True" and stock_instance == False:
      # START STOCK LOOP AGAIN
      user_soft = await check_db("stock_user")
      user = bot.get_user(user_soft)
      countdown = await check_db("stock_countdown")
      countdown = int(countdown)
      channel_soft = await check_db("stock_channel")
      channel = await bot.get_channel(int(channel_soft))
      old = stock_info.get_live_price(interest)
      for i in range(100):
        if stock_instance == True:
          await asyncio.sleep(60*countdown)
          current = stock_info.get_live_price(interest)
          percentage = old - current
          percentage = percentage / old
          percentage = percentage * 100
          await channel.send(user.mention + ", " + interest + ": **" + str(current) + "** (change: **" + str(percentage) + "%**)")
        else:
          break
      
    
