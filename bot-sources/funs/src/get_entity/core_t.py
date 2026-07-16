from aiogram import Bot
from aiogram import Router

# funs
from funs.get_entity.config_t import get_token

# storage
import storage.core

# code
async def get_bot_src():
    if storage.core.bot == None:
        storage.core.bot = Bot(get_token())
    return storage.core.bot

async def get_router_src():
    if storage.core.router == None:
        storage.core.router = Router()
    return storage.core.router