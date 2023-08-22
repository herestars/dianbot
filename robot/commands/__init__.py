from khl import Message, Bot
import traceback
from robot.loader import bot, redis
from loguru import logger
from lib import send_to_openai_async
from khl import ChannelPrivacyTypes
import config
import json

logger.info("Loading commands...")


def is_admin(msg: Message):
    return msg.author.id == "3335682013"


@bot.command(rules=[is_admin])
async def gaming(msg: Message, game_id: int):
    # game_id : int
    await bot.client.update_playing_game(game_id)
    await msg.reply("gaming!")


@bot.command(rules=[is_admin])
async def music(msg: Message, music: str, singer: str):
    # music name : str
    # singer name : str
    # music_software : Enum ['cloudmusic'、'qqmusic'、'kugou'], 'cloudmusic' in default
    await bot.client.update_listening_music(music, singer, "qqmusic")
    await msg.reply("listening to music!")


@bot.command(name="hello", prefixes=("/", "#"), rules=[is_admin])
async def world(msg: Message):
    await msg.reply("world!")


@bot.command(name="game-s")
async def game_search_cmd(msg: Message, game_name: str):
    try:
        print("get /game-s cmd")
        games = await bot.client.fetch_game_list()
        target_games = []  # 结果列表
        # 遍历查找
        for g in games:
            # 使用模糊匹配，只要用户需要查找的游戏名字包含在其中，就添加到结果列表中
            if game_name.lower() in g.name.lower():
                target_games.append(g)  # 插入 Game 对象

        # list 为空代表没有找到
        if target_games == []:
            await msg.reply(f"没有找到「{game_name}」游戏")
        else:
            text = f"找到了「{game_name}」游戏\n"
            for game in target_games:
                text += "```\n"
                text += f"ID：{game.id}\n"
                text += f"名字：{game.name}\n"
                text += f"类型：{game.type}\n"
                text += "```\n"
            text += f"共「{len(target_games)}」个结果"
            await msg.reply(text)
    except:
        print(traceback.format_exc())  # 如果出现异常，打印错误


chat_channel_id = ["3980462878546253", "1472424805587532"]
my_id = None


@bot.on_message()
async def on_message(msg: Message):
    global my_id
    if my_id is None:
        my_id = (await bot.fetch_me()).id
    previous_msg_to = None
    if (
        msg.channel_type == ChannelPrivacyTypes.GROUP
        and msg.target_id in chat_channel_id
    ):
        previous_msg_to = redis.get(f"previous_msg_to_{msg.target_id}")
        if previous_msg_to:
            previous_msg_to = str(previous_msg_to, encoding="utf-8")
        
    # if we chat with bot in a chat channel and we chat with bot continuously, we may not required to mention bot every time
    if (
        msg.channel_type == ChannelPrivacyTypes.GROUP
        and msg.target_id in chat_channel_id
        and (
            my_id in msg.extra.get("mention")
            or (previous_msg_to == msg.author.id and msg.extra.get("mention") == [])
        )
    ) or (msg.channel_type == ChannelPrivacyTypes.PERSON and is_admin(msg)):
        # get chat msg from redis
        chat_msg = []
        author_msgs = redis.get(msg.author.id)
        if author_msgs:
            chat_msg = json.loads(str(author_msgs, encoding="utf-8"))

        # remove mention
        content = msg.content.replace(f"(met){my_id}(met)", "")

        # add to chat msg and remove old msg
        chat_msg.append({"role": "user", "content": content})
        while len(chat_msg) > 30:
            chat_msg.pop(0)

        # send to openai and get reply
        reply_text = await send_to_openai_async(chat_msg)
        chat_msg.append({"role": "assistant", "content": reply_text})

        # save chat msg to redis
        redis.setex(msg.author.id, 60 * 60, json.dumps(chat_msg))
        redis.setex(f"previous_msg_to_{msg.target_id}", 60 * 60, msg.author.id)

        # send reply
        previous_msg_to = msg.author.id
        await msg.reply(reply_text)
    elif (msg.channel_type == ChannelPrivacyTypes.GROUP and msg.target_id in chat_channel_id):
        redis.delete(f"previous_msg_to_{msg.target_id}")
        

async def handle_startup(bot: Bot):
    logger.info("Bot started!")
    log_channel = await bot.client.fetch_public_channel(config.LOG_CHANNEL_ID)
    await log_channel.send(f"Bot started!")


bot.on_startup(handle_startup)
