#!/usr/bin/env python
from dotenv import load_dotenv
import asyncio
from aiohttp import web
from bot import get_bot
from web import get_app
import config

if __name__ == "__main__":
    bot = get_bot()
    app = get_app()
    app["bot"] = bot

    asyncio.get_event_loop().run_until_complete(
        asyncio.gather(web._run_app(app, host=config.WEB_HOST, port=config.WEB_PORT), bot.start())
    )
