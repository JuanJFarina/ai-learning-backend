from ai_learning.domain import BaseLLMClient
from google import genai
from ai_learning.settings import Settings
from typing import Any


class GoogleClient(BaseLLMClient):
    def __init__(self) -> None:
        self.client = genai.Client(api_key=Settings.GOOGLE_API_KEY)

    def generate(self, model_name: str, prompt: str, **kwargs: Any) -> str:
        response = self.client.models.generate_content(
            model=model_name,
            contents=prompt,
            **kwargs,
        )
        return response.candidates[0].content.parts[0].text  # type: ignore
