from ai_learning.domain import AITeacher, BaseLLMClient, Lesson
from ai_learning.settings import Settings


def create_lesson(
    llm_client: BaseLLMClient,
    topic: str,
    concept: str,
) -> Lesson:
    ai_teacher = AITeacher(llm_api_client=llm_client, model_name=Settings.MODEL_NAME)
    lesson = ai_teacher.create_lesson(topic, concept)
    if lesson:
        return lesson
    raise ValueError("Failed to create lesson")
