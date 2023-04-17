from typing import List

import click
import sienna
from tqdm import tqdm

from rougek.extract.utils import get_ngram_overlaps


@click.command()
@click.argument("dpath")
@click.argument("opath")
def extract(dpath: str, opath: str) -> None:
    """Command to generate a list of keywords"""
    data = sienna.load(dpath)
    assert isinstance(data, list)
    assert isinstance(data[0], dict)

    result_ngrams_li: List[List[str]] = []
    for d in tqdm(data):
        refs = d["target"]
        if len(refs):
            refs += [d["title"]]
        assert isinstance(refs, list), f"Wrong format., type(refs)=={type(refs)}"
        assert len(refs) >= 2, f"Refs too small. len(refs)=={len(refs)}"
        assert isinstance(
            refs[0], str
        ), f"Wrong format., type(refs[0])=={type(refs[0])}"

        ngrams = get_ngram_overlaps(refs, 10)
        ngrams_str = [" ".join(ngram) for ngram in ngrams]
        result_ngrams_li.append(ngrams_str)

    print(f"Saving keyword list to {opath}...")
    sienna.save(result_ngrams_li, opath)
