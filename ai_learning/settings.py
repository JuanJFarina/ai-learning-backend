from pydantic_settings import BaseSettings, SettingsConfigDict

from ai_learning.domain import SupportedModels


class _Settings(BaseSettings):
    GOOGLE_API_KEY: str = ""
    MODEL_NAME: SupportedModels = SupportedModels.GEMINI_2_0_FLASH

    model_config = SettingsConfigDict(
        env_file=".env",
    )


Settings = _Settings()
