from ai_learning.domain.models import LessonConcept


def get_previous_lessons_prompt(
    first: LessonConcept,
    second: LessonConcept,
    third: LessonConcept,
) -> str:
    if not any([first, second, third]):
        print(first, second, third)
        return ""
    return f"""
The student comes from studying these lessons:
- "{first.topic}" and the concept of "{first.concept}"
- "{second.topic}" and the concept of "{second.concept}"
- "{third.topic}" and the concept of "{third.concept}"
"""
