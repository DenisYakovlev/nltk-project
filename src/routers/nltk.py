from typing import Any, List, Tuple

from fastapi import APIRouter

from schemas import (NerResponseSchema, PosTagResponseSchema, TextSchema,
                     TokenizeResponseSchema)
from services import nltk_tools

router = APIRouter()


@router.post("/tokenize/", response_model=TokenizeResponseSchema)
async def tokenize(input: TextSchema):
    """
    Tokenizes the input text.
    """

    tokens: List[str] = nltk_tools.tokenize_text(input.text)
    return {"tokens": tokens}


@router.post("/pos_tag/", response_model=PosTagResponseSchema)
async def post_tag(input: TextSchema):
    """
    Performs part-of-speech tagging on the input text.
    """

    tagged_tokens: List[Tuple[Any, str]] = nltk_tools.pos_tag(input.text)
    return {"tagged_tokens": tagged_tokens}


@router.post("/ner/", response_model=NerResponseSchema)
async def ner(input: TextSchema):
    """
    Performs named entity recognition (NER) on the input text.
    """

    named_entities = nltk_tools.ner(input.text)
    return {"named_entities": named_entities}
