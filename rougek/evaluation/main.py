from typing import List

from _rougek import filter_stopwords, find

from rougek.utils.stopwords import filter_stopwords
from rougek.utils.tokenizer import get_preprocessor


class RougeK:
    """Compute ROUGE-K score for given hypo and keywords

    Attributes
    ----------
    preprocessor : Customized spacy-based preprocessor
    """

    def __init__(self):
        self.preprocessor = get_preprocessor()

    def __call__(self, hypo: str, kws: List[str]) -> float:
        """Computes ROUGE-K for given hypo and gold kws

        Parameters
        ----------
        hypo : str
            Target summary to evaluate
        kws : List[str]
            Gold keywords to match with summary

        Returns
        -------
        float
            ROUGE-K score
        """
        words = self.preprocessor(hypo)
        words = filter_stopwords(words)

        cnt = 0
        for kw in kws:
            if find(" ".join(words), kw):
                cnt += 1

        return cnt / len(kws)
