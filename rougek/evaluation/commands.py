import os

import click
import sienna

from rougek import RougeK
from rougek.utils.utils import avg, std


def evaluate_hypo_file(hypo_path: str, kws_li: list[list[str]]) -> list[float]:
    hypos = sienna.load(hypo_path)
    assert isinstance(hypos, list)
    assert isinstance(hypos[0], str)
    return evaluate_hypos(hypos, kws_li)


def evaluate_hypos(hypos: list[str], kws_li: list[list[str]]) -> list[float]:
    rk = RougeK()
    rk_scores: list[float] = []
    for hypo, kws in zip(hypos, kws_li):
        rk_scores.append(rk(hypo, kws))
    return rk_scores


@click.command()
@click.argument("hypo_path")
@click.argument("kws_path")
def evaluate(hypo_path: str, kws_path: str) -> None:
    """Command to evaluate summaries by ROUGE-K"""
    rk = RougeK()

    hypos = sienna.load(hypo_path)
    kws_li = sienna.load(kws_path)

    assert isinstance(hypos, list) & isinstance(hypos[0], str)
    assert isinstance(kws_li, list) & isinstance(kws_li[0], list)

    rk_scores = []

    for hypo, kws in zip(hypos, kws_li):
        rk_scores.append(rk(hypo, kws))

    print(f"Avg ROUGE-K is: {avg(rk_scores)}±{std(rk_scores)}")


@click.command()
@click.argument("hypo_dir")
@click.argument("kws_path")
def evaluate_dir(hypo_dir: str, kws_path: str) -> None:
    """Command to evaluate summaries by ROUGE-K"""
    hypo_paths = [
        os.path.join(hypo_dir, hypo_filename)
        for hypo_filename in os.listdir(hypo_dir)
        if hypo_filename.endswith(".hypo")
    ]
    
    print(f"{len(hypo_paths)} target file found.")

    kws_li = sienna.load(kws_path)
    assert isinstance(kws_li, list)
    assert isinstance(kws_li[0], list)

    hypo_scores = []
    for hypo_path in hypo_paths:
        rk_scores = evaluate_hypo_file(hypo_path, kws_li)
        hypo_scores.append(avg(rk_scores))

    print(f"Avg ROUGE-K is: {avg(hypo_scores)}±{std(hypo_scores)}")
