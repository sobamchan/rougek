from collections import Counter
from typing import List, Set, Tuple

import nltk

from rougek.utils.stopwords import filter_stopwords
from rougek.utils.tokenizer import get_preprocessor


def build_ngrams(tokens: List[str], ngram_n: int) -> Set[Tuple[str, ...]]:
    ngrams = list(nltk.ngrams(tokens, ngram_n))
    clean_ngrams = [tuple(filter_stopwords(ngram)) for ngram in ngrams]
    clean_ngrams = [ngrams for ngrams in clean_ngrams if len(ngrams) != 0]
    return set(clean_ngrams)


def get_overlaps(refs: List[str], ngram_n: int) -> List[Tuple[str, ...]]:
    preprocessor = get_preprocessor()
    more_than_n = 2
    set_ngrams_li = [build_ngrams(preprocessor(ref), ngram_n) for ref in refs]
    ngrams = [ngram for set_ngrams in set_ngrams_li for ngram in set_ngrams]
    return [ngram for ngram, cnt in Counter(ngrams).items() if cnt >= more_than_n]


def get_ngram_overlaps(refs: List[str], max_ngram_n: int) -> List[Tuple[str, ...]]:
    """Extract ngram overlaps between reference summaries

    Parameters
    ----------
    refs : List[str]
        List of reference summaries
    max_ngram_n : int
        Upper bound of ngram length

    Returns
    -------
    List[Tuple[str, ...]]
        List of extracted keywords
    """
    selected_ngrams = []
    vocab = []
    for n in range(max_ngram_n, 0, -1):
        ngrams = get_overlaps(refs, n)
        for ngram in ngrams:
            is_to_add = True
            for word in ngram:
                if word in vocab:
                    is_to_add = False
            if is_to_add:
                selected_ngrams.append(ngram)
                vocab += list(ngram)
    return selected_ngrams
