import pytest
from unittest.mock import AsyncMock, patch
from bot.services.chat import ChatService


@pytest.fixture
def chat_service():
    with patch("bot.services.chat.AsyncOpenAI"):
        return ChatService(api_key="test-key")


@pytest.mark.asyncio
async def test_chat(chat_service):
    mock_response = AsyncMock()
    mock_response.choices = [AsyncMock()]
    mock_response.choices[0].message.content = "Привет! Чем могу помочь?"
    chat_service.client.chat.completions.create = AsyncMock(return_value=mock_response)

    response = await chat_service.chat(123, "Привет", [])

    assert "Привет" in response
    assert len(response) > 0


@pytest.mark.asyncio
async def test_chat_with_history(chat_service):
    mock_response = AsyncMock()
    mock_response.choices = [AsyncMock()]
    mock_response.choices[0].message.content = "Хорошо, продолжаю тему"
    chat_service.client.chat.completions.create = AsyncMock(return_value=mock_response)

    history = [
        {"role": "user", "content": "Расскажи про Python"},
        {"role": "assistant", "content": "Python — популярный язык программирования"},
    ]

    response = await chat_service.chat(123, "А что насчёт JavaScript?", history)

    assert len(response) > 0
