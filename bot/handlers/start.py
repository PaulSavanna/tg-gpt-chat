from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()


def get_main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎨 Генерация картинки", callback_data="image")],
        [InlineKeyboardButton(text="🗑️ Очистить историю", callback_data="clear")],
        [InlineKeyboardButton(text="❓ Помощь", callback_data="help")],
    ])


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 Привет! Я GPT чат-бот с генерацией картинок.\n\n"
        "Просто напиши мне что угодно — и я отвечу.\n"
        "Нажми «Генерация картинки» — и я нарисую по описанию.",
        reply_markup=get_main_menu()
    )


@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "📝 Как пользоваться:\n\n"
        "• Просто напиши сообщение — я отвечу\n"
        "• Пришли фото с подписью — опишу что вижу\n"
        "• Нажми «Генерация картинки» — нарисую по описанию\n"
        "• История контекста сохраняется\n\n"
        "Команды:\n"
        "/start — начать заново\n"
        "/image <описание> — сгенерировать картинку\n"
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
        "• Нажми «Генерация картинки» — нарисую по описанию\n"
        "• История контекста сохраняется",
        reply_markup=get_main_menu()
    )
    await callback.answer()


@router.callback_query(lambda c: c.data == "image")
async def callback_image(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "🎨 Напиши описание картинки, которую я должен нарисовать.\n\n"
        "Примеры:\n"
        "• «кот в космосе»\n"
        "• «пейзаж гор на закате в стиле аниме»\n"
        "• «логотип для техно-бара»",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="◀️ Назад", callback_data="back")]
        ])
    )
    await callback.answer()


@router.callback_query(lambda c: c.data == "back")
async def callback_back(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Выбери действие или напиши сообщение:",
        reply_markup=get_main_menu()
    )
    await callback.answer()
