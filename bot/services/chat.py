from openai import AsyncOpenAI


class ChatService:
    def __init__(self, api_key: str):
        self.client = AsyncOpenAI(api_key=api_key)
        self.system_prompt = (
            "Ты полезный AI-ассистент. Отвечай на русском языке. "
            "Будь дружелюбным и помогай пользователю."
        )

    async def chat(self, user_id: int, message: str, history: list[dict]) -> str:
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend(history)
        messages.append({"role": "user", "content": message})

        response = await self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=2000,
        )
        return response.choices[0].message.content

    async def chat_with_image(self, user_id: int, message: str, image_url: str, history: list[dict]) -> str:
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend(history)
        messages.append({
            "role": "user",
            "content": [
                {"type": "text", "text": message},
                {"type": "image_url", "image_url": {"url": image_url}},
            ],
        })

        response = await self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=2000,
        )
        return response.choices[0].message.content
