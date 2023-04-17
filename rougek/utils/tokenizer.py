from functools import partial
from typing import Callable, List

import spacy
from spacy.lang.char_classes import (ALPHA, ALPHA_LOWER, ALPHA_UPPER,
                                     CONCAT_QUOTES, LIST_ELLIPSES, LIST_ICONS)
from spacy.tokenizer import Tokenizer
from spacy.util import compile_infix_regex


def custom_tokenizer(spacy_nlp):
    infixes = (
        LIST_ELLIPSES
        + LIST_ICONS
        + [
            r"(?<=[0-9])[+\-\*^](?=[0-9-])",
            r"(?<=[{al}{q}])\.(?=[{au}{q}])".format(
                al=ALPHA_LOWER, au=ALPHA_UPPER, q=CONCAT_QUOTES
            ),
            r"(?<=[{a}]),(?=[{a}])".format(a=ALPHA),
            # r"(?<=[{a}])(?:{h})(?=[{a}])".format(a=ALPHA, h=HYPHENS),
            r"(?<=[{a}0-9])[:<>=/](?=[{a}])".format(a=ALPHA),
        ]
    )

    infix_re = compile_infix_regex(infixes)

    return Tokenizer(
        spacy_nlp.vocab,
        prefix_search=spacy_nlp.tokenizer.prefix_search,
        suffix_search=spacy_nlp.tokenizer.suffix_search,
        infix_finditer=infix_re.finditer,
        token_match=spacy_nlp.tokenizer.token_match,
        rules=spacy_nlp.Defaults.tokenizer_exceptions,
    )


def preprocess(nlp: Tokenizer, sent: str) -> List[str]:
    """Given a sentence, clean and return list of ngrams"""
    sent = sent.lower()
    tokens = [
        token.lemma_ if token.lemma_ != "-PRON-" else token.orth_ for token in nlp(sent)
    ]
    return tokens


def get_preprocessor() -> Callable:
    """Get preprocessor that lower and tokenize texts

    Returns
    -------
    Callable
        A callable function that takes str and return words (List[str])
    """
    spacy_nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])
    spacy_nlp.tokenizer = custom_tokenizer(spacy_nlp)
    return partial(preprocess, spacy_nlp)
