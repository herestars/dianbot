#!/usr/bin/env python
import nonebot
from nonebot.adapters.kaiheila import Adapter as KaiheilaAdapter
from nonebot import require

nonebot.init()
require("nonebot_plugin_apscheduler")

driver = nonebot.get_driver()

driver.register_adapter(KaiheilaAdapter)

import tasks

tasks.load_task() 

nonebot.load_builtin_plugins("echo") 

if __name__ == "__main__":
    nonebot.run()