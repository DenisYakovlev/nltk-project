from typing import Any, List, Tuple

import nltk


def tokenize_text(text: str) -> List[str]:
    # modify this for more language options
    return nltk.tokenize.word_tokenize(text)


def pos_tag(text: str) -> List[Tuple[Any, str]]:
    tokens: List[str] = tokenize_text(text)
    return nltk.tag.pos_tag(tokens)


def ner(text: str):
    tagged_tokens = pos_tag(text)
    named_entities = nltk.chunk.ne_chunk(tagged_tokens)

    # extract entities
    entities = []
    for chunk in named_entities:
        if hasattr(chunk, 'label'):
            entity = ' '.join(c[0] for c in chunk)
            entity_type = chunk.label()
            entities.append({
                "entity": entity,
                "entity_type": entity_type
            })

    return entities
