import pytest
from bot.services.database import Database


@pytest.fixture
def db(tmp_path):
    return Database(str(tmp_path / "test.db"))


@pytest.mark.asyncio
async def test_init_db(db):
    await db.init()
    history = await db.get_history(123)
    assert history == []


@pytest.mark.asyncio
async def test_add_and_get_message(db):
    await db.init()
    await db.add_message(123, "user", "Привет")
    await db.add_message(123, "assistant", "Привет! Чем могу помочь?")

    history = await db.get_history(123)
    assert len(history) == 2
    roles = {msg["role"] for msg in history}
    assert "user" in roles
    assert "assistant" in roles


@pytest.mark.asyncio
async def test_clear_history(db):
    await db.init()
    await db.add_message(123, "user", "Тест")
    await db.clear_history(123)

    history = await db.get_history(123)
    assert history == []


@pytest.mark.asyncio
async def test_separate_users(db):
    await db.init()
    await db.add_message(1, "user", "Сообщение 1")
    await db.add_message(2, "user", "Сообщение 2")

    history1 = await db.get_history(1)
    history2 = await db.get_history(2)

    assert len(history1) == 1
    assert len(history2) == 1
    assert history1[0]["content"] == "Сообщение 1"
    assert history2[0]["content"] == "Сообщение 2"
