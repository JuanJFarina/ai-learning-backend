from .base_client import BaseClient
from google import genai
from ai_learning.settings import Settings
from typing import ParamSpecKwargs
from google.genai import types


class GoogleClient(BaseClient):
    def __init__(self) -> None:
        self.client = genai.Client(api_key=Settings.GOOGLE_API_KEY)

    def generate(self, model_name: str, prompt: str, **kwargs: ParamSpecKwargs) -> str:
        response = self.client.models.generate_content(
            model="gemini-2.0-flash-exp-image-generation",
            contents=prompt,
            config=types.GenerateContentConfig(response_modalities=["TEXT", "IMAGE"]),
        )
        return response.candidates[0].content.parts.text  # TODO: create a pydantic model
