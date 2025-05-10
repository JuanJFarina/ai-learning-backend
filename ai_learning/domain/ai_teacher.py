from google.genai import types
import json
from dataclasses import field
from datetime import datetime

from .base_client import BaseLLMClient
from ai_learning.utils import retry

from .models import SupportedModels

from .models import Lesson, LessonConcept
from .prompts import (
    get_base_prompt,
    get_previous_lessons_prompt,
    get_current_lesson_prompt,
)


class AITeacher:
    def __init__(self, llm_api_client: BaseLLMClient, model_name: SupportedModels):
        self.api_client = llm_api_client
        self.model_name = model_name

    @retry()
    def create_lesson(
        self,
        topic: str,
        concept: str,
        previous_lessons: list[LessonConcept] = field(default_factory=list),
    ) -> Lesson:
        prompt = self._create_lesson_prompt(topic, concept, previous_lessons)
        response = self.api_client.generate(
            model_name=self.model_name,
            prompt=prompt,
            config=types.GenerateContentConfig(response_modalities=["TEXT"]),
        )
        return self._raw_response_to_lesson(response)

    def _create_lesson_prompt(
        self, topic: str, concept: str, previous_lessons: list[LessonConcept]
    ) -> str:
        prompt = get_base_prompt()
        if len(previous_lessons) == 3:
            prompt += get_previous_lessons_prompt(*previous_lessons)
        prompt += get_current_lesson_prompt(topic, concept)
        return prompt

    def _raw_response_to_lesson(self, raw_response: str) -> Lesson:
        json_response = json.loads(raw_response)
        json_response["created_at"] = datetime.now().isoformat()
        print("Attempting to validate Lesson")
        return Lesson.model_validate(json_response)
