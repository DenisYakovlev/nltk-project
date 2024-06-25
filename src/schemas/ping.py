from pydantic import BaseModel


class PingSchema(BaseModel):
    msg: str
