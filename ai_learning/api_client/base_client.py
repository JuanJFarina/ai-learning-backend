from abc import ABC
from typing import ParamSpecKwargs

class BaseClient(ABC):
    def generate(self, model_name: str, prompt: str, **kwargs: ParamSpecKwargs) -> str:
        raise NotImplementedError("Subclasses must implement this method")
