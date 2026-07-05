from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()


def get_main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🗑️ Очистить историю", callback_data="clear")],
        [InlineKeyboardButton(text="❓ Помощь", callback_data="help")],
    ])


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 Привет! Я GPT чат-бот.\n\n"
        "Просто напиши мне что угодно — и я отвечу.\n"
        "Также могу анализировать фото, если пришлёшь картинку.",
        reply_markup=get_main_menu()
    )


@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "📝 Как пользоваться:\n\n"
        "• Просто напиши сообщение — я отвечу\n"
        "• Пришли фото с подписью — опишу что вижу\n"
        "• История контекста сохраняется\n\n"
        "Команды:\n"
        "/start — начать заново\n"
        "/clear — очистить историю\n"
        "/help — помощь",
        reply_markup=get_main_menu()
    )


@router.callback_query(lambda c: c.data == "help")
async def callback_help(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "📝 Как пользоваться:\n\n"
        "• Просто напиши сообщение — я отвечу\n"
        "• Пришли фото с подписью — опишу что вижу\n"
        "• История контекста сохраняется",
        reply_markup=get_main_menu()
    )
    await callback.answer()
