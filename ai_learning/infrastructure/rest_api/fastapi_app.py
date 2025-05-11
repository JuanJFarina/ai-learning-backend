from fastapi import FastAPI, Path
from ai_learning import __version__ as curr_version
from ai_learning.application import create_lesson
from ai_learning.domain import Lesson, StudyTopics
from ai_learning.infrastructure import GoogleClient
from .models import HealthcheckResponse
from typing import Annotated


app = FastAPI(
    title="AI Learning",
    description="AI Learning REST API",
    version=curr_version,
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
)


@app.get("/healthcheck", response_model=HealthcheckResponse)
async def healthcheck() -> dict[str, dict[str, Any]]:
    return {
        "message": {
            "status": "ok",
            "version": curr_version,
            "endpoints": app.openapi().get("paths"),
        }
    }


@app.get("/lessons/{topic}/{concept}", response_model=Lesson)
async def get_lesson(
    topic: StudyTopics, concept: Annotated[str, Path(min_length=2, max_length=30)]
) -> Lesson:
    llm_api_client = (
        GoogleClient()
    )  # TODO: implement a dependency injection framework in the create_lesson function
    return create_lesson(llm_api_client, topic, concept)
