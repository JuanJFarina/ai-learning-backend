from pydantic import BaseModel, Field
from uuid import UUID, uuid4

from .study_topics import StudyTopics


class LessonConcept(BaseModel):
    topic: StudyTopics
    concept: str


class LessonReference(LessonConcept):
    description: str
    id: UUID = Field(default_factory=uuid4)


class Lesson(LessonReference):
    full_text: str
    mermaid_diagram: str
    references: list[str]
    related_lessons: list[LessonConcept]
    created_at: str

    def get_reference(self) -> LessonReference:
        return LessonReference(
            topic=self.topic,
            concept=self.concept,
            description=self.description,
        )
