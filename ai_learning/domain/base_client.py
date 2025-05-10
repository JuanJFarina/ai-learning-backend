from abc import ABC
from typing import Any


class BaseLLMClient(ABC):
    def generate(self, model_name: str, prompt: str, **kwargs: Any) -> str:
        raise NotImplementedError("Subclasses must implement this method")
