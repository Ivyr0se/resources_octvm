
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
        await roles.append(str(role))
    return roles
