
import nonebot
from nonebot_plugin_apscheduler import scheduler

async def send_msg():
    bot = nonebot.get_bot()
    await bot.send_msg("Hello World")

def load_task():
    # scheduler.add_job(send_msg, 'interval', minutes=1, id='send_msg')
    pass