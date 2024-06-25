from typing import Any, Dict, List, Tuple

from pydantic import BaseModel


class TextSchema(BaseModel):
    text: str


class TokenizeResponseSchema(BaseModel):
    tokens: List[str]


class PosTagResponseSchema(BaseModel):
    tagged_tokens: List[Tuple[Any, str]]


class NerResponseSchema(BaseModel):
    named_entities: List[Dict[str, str]]
