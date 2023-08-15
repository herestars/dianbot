#!/usr/bin/env python
import traceback
from khl import Bot, Message
from dotenv import dotenv_values
import os

config = {
    **dotenv_values(".env"),  # load shared development variables
    **dotenv_values(".env.dev"),  # load sensitive variables
    #**os.environ,  # override loaded values with environment variables
}

if os.environ.get("env") == 'enable':
    config = {**config, **os.environ}

bot = Bot(token=config["token"], port=config["port"])


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
            text += """
```cpp
#include <bits/stdc++.h>

int main(){
    cout << "Hello World" << endl;
    return 0;
}
```
"""

            # 更多游戏信息参考 https://developer.kookapp.cn/doc/http/game 对 game 对象的定义
            # 机器只需要获取到 game.id ，就能上在玩状态
            await msg.reply(text)
    except:
        print(traceback.format_exc())  # 如果出现异常，打印错误

if __name__ == "__main__":
    bot.run()