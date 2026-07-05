from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.services.chat import ChatService
from bot.services.database import Database
from bot.config import settings

router = Router()
chat_service = ChatService(api_key=settings.openai_api_key)
db = Database(settings.db_path)


def get_main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🗑️ Очистить историю", callback_data="clear")],
    ])


@router.callback_query(lambda c: c.data == "clear")
async def callback_clear(callback: types.CallbackQuery):
    await db.clear_history(callback.from_user.id)
    await callback.message.edit_text(
        "🗑️ История очищена! Начни новый разговор.",
        reply_markup=get_main_menu()
    )
    await callback.answer()


@router.message(Command("clear"))
async def cmd_clear(message: types.Message):
    await db.clear_history(message.from_user.id)
    await message.answer(
        "🗑️ История очищена!",
        reply_markup=get_main_menu()
    )


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    from bot.handlers.start import cmd_start as start_cmd
    await start_cmd(message)


@router.message(Command("help"))
async def cmd_help(message: types.Message):
    from bot.handlers.start import cmd_help as help_cmd
    await help_cmd(message)


@router.message()
async def handle_message(message: types.Message):
    user_id = message.from_user.id

    if message.photo:
        photo = message.photo[-1]
        file = await message.bot.get_file(photo.file_id)
        file_url = f"https://api.telegram.org/file/bot{settings.bot_token}/{file.file_path}"

        text = message.caption or "Опиши что ты видишь на этом фото"
        history = await db.get_history(user_id)

        await db.add_message(user_id, "user", f"[Фото] {text}")

        response = await chat_service.chat_with_image(user_id, text, file_url, history)

        await db.add_message(user_id, "assistant", response)
        await message.answer(response, reply_markup=get_main_menu())
        return

    text = message.text.strip()
    if not text:
        return

    await db.add_message(user_id, "user", text)

    history = await db.get_history(user_id)

    response = await chat_service.chat(user_id, text, history)

    await db.add_message(user_id, "assistant", response)
    await message.answer(response, reply_markup=get_main_menu())
