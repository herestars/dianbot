#!/usr/bin/env python
from loguru import logger
import asyncio
from aiohttp import web
from robot import bot
from web import get_app
import config


if __name__ == "__main__":
    app = get_app()
    app["bot"] = bot
    asyncio.get_event_loop().run_until_complete(
        asyncio.gather(web._run_app(app, host=config.WEB_HOST, port=config.WEB_PORT), bot.start())
    )
