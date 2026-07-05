from dataclasses import dataclass
from dotenv import load_dotenv
import os


@dataclass(frozen=True)
class Settings:
    bot_token: str
    openai_api_key: str
    db_path: str = "chat.db"

    @classmethod
    def from_env(cls) -> "Settings":
        load_dotenv()
        return cls(
            bot_token=os.environ["BOT_TOKEN"],
            openai_api_key=os.environ["OPENAI_API_KEY"],
        )


settings = Settings.from_env()
