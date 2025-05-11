from pydantic import BaseModel


class HealthcheckMessage(BaseModel):
    status: str
    version: str
    endpoints: dict[str, dict[str, str]]


class HealthcheckResponse(BaseModel):
    message: HealthcheckMessage
