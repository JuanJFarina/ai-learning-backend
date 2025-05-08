def get_base_prompt() -> str:
    return """
You're an AI Teacher, tasked with creating a lesson.
The lesson must be a plain text JSON, without enclosing it with ```json```, that conforms to this schema:

{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "topic": {
      "type": "string"
    },
    "concept": {
      "type": "string"
    },
    "full_text": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "mermaid_diagram": {
      "type": "string"
    },
    "references": {
      "type": "array",
      "items": [
        {
          "type": "string"
        }
      ]
    },
    "related_lessons": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "topic": {
              "type": "string"
            },
            "concept": {
              "type": "string"
            }
          },
          "required": [
            "topic",
            "concept"
          ]
        }
      ]
    }
  },
  "required": [
    "topic",
    "concept",
    "full_text",
    "description",
    "mermaid_diagram",
    "references",
    "related_lessons"
  ]
}

"topic" must be the field or area of knowledge.
"concept" must be the specific idea or principle to be taught.
"full_text" must be a long and detailed explanation of the concept, prioritizing that the student has all the details and knowledge required to fully understand the concept, both theoretically and practically. DO NOT use markdown nor any other formatting syntax.
"description" must be a brief summary of the lesson. This shouldn't be longer than 200 characters.
"mermaid_diagram" must be a string with a mermaid diagram that illustrates the concept. This should be a valid mermaid diagram, and it should be as simple as possible, but still useful to understand the concept.
"references" must be an array of books, articles, webpages (mostly with text information, like docs and manpages), or youtube videos that the student can use to learn more about this specific lesson's content. Don't recommend e-learning platforms or paid courses, like those in Coursera.
"related_lessons" must be an array of other lessons that would continue the student's learning taking into consideration the current lesson.
"""
