from khl import Bot, Message
import os
import traceback
import random
import config
from enum import Enum

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


class UpdateState(Enum):
    NO_UPDATE = "no update"
    PLAY_GAME = "play game"
    LISTEN_MUSIC = "listen music"
    SLEEP = "sleep"


def get_bot():
    bot = Bot(token=config.KOOK_TOKEN)

    @bot.task.add_interval(minutes=config.STATE_CHECK_INTERVAL_MINUTES)
    async def update_status():
        state = random.choices(
            [
                UpdateState.NO_UPDATE,
                UpdateState.PLAY_GAME,
                UpdateState.SLEEP,
            ],
            weights=[0.2, 0.5, 0.2],
        )
        logger.info(f"update bot status: {state[0].value}")
        match state[0]:
            case UpdateState.NO_UPDATE:
                return
            case UpdateState.PLAY_GAME:
                game = random.choice(config.PLAYING_GAMES)
                logger.info(f"update bot playing game: {game[1]}")
                await bot.client.update_playing_game(game[0])
                return
            case UpdateState.SLEEP:
                try:
                    await bot.client.stop_listening_music()
                except:
                    pass
                try:
                    await bot.client.stop_playing_game()
                except:
                    pass
                return

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

    return bot
