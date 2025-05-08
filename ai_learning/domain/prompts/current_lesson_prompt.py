def get_current_lesson_prompt(
    topic: str,
    concept: str,
) -> str:
    return f"""
Now create a lesson on the topic of "{topic}" and the concept of "{concept}".

Remember, your answer must have the specified JSON format, without any text or explanation outside of it.
"""
