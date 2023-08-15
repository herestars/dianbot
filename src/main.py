#!/usr/bin/env python
import traceback
from dotenv import load_dotenv
import os
import asyncio
from aiohttp import web, web_request
from bot import get_bot
from web import get_app

load_dotenv()

HOST, PORT = "0.0.0.0", 4396

if __name__ == "__main__":

    bot = get_bot()
    app = get_app()
    asyncio.get_event_loop().run_until_complete(
        asyncio.gather(web._run_app(app, host=HOST, port=PORT), bot.start())
    )
