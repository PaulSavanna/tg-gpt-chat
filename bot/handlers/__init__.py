from aiogram import Router

from bot.handlers.start import router as start_router
from bot.handlers.chat import router as chat_router

def setup_handlers(dp: Router):
    dp.include_router(start_router)
    dp.include_router(chat_router)
