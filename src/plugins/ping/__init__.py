from nonebot import get_driver
from nonebot import on_command
import nonebot
from nonebot.adapters import Message,Event
from nonebot.matcher import Matcher
from .config import Config
from nonebot.params import Arg, ArgPlainText, CommandArg
global_config = get_driver().config
config = Config.parse_obj(global_config)

# Export something for other plugin
# export = nonebot.export()
# export.foo = "bar"

# @export.xxx
# def some_function():
#     pass

ping = on_command("ping", priority=5)
@ping.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    bot = nonebot.get_bots()['1132485606']
    await bot.call_api("send_friend_message", target=49451799, message_chain=[{"type":"Plain", "text":"Hello\n"}])
    #await bot.call_api("about")
    await ping.finish("pong")