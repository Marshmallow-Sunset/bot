from aiogram import Bot
from aiogram import Router

# funs
from funs.get_entity.config_t import get_token

# storage
import storage.core

async def get_bot_src():
    try:
        if storage.core.bot == None:
            storage.core.bot = Bot(get_token())
        return storage.core.bot
    except Exception as e:
        print(f"get_bot(): {e}")
        return

async def get_router_src():
    try:
        if storage.core.router == None:
            storage.core.router = Router()
        return storage.core.router
    except Exception as e:
        print(f"get_router: {e}")
        return