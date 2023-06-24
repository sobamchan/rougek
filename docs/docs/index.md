# ROUGE-K

ROUGE-K is an extension of ROUGE metrics with a focus on keywords enabling developers to know: *How well the summarizer includes keywords in outputs.*

You can use this library to build a list of keywords from your summarization datasets and use them to evaluate the generated summaries using ROUGE-K.


# Installation

```sh
pip install rougek
```


# Usage

There are two steps to follow to evaluate your summaries with ROUGE-K, 1. keyword extraction, 2. evaluation.


## Keyword extraction

The source dataset needs to be a jsonline file which contains a json object in each line.
Each sample in input files need three information, (1) `source (List[str])`: List of sentences in source document, (2) `target (List[str])`: List of reference summaries, it can be a list with just one element (one sentence) if there is only one reference summary in your dataset, (3) `title (str)`: title of the source documents.

Try with a sample dataset file by running the following command.

```sh
rougek extract ./tests/sample.jsonl output.jsonl
```

Resulting data (`output.jsonl`) is also a jsonline file, each line contains a list of keywords (`List[str]`).
This file will be used in the next evaluation step.


## Evaluation

You can evaluate your summaries by ROUGE-K in your python scripts as follows:

### From python

```py
from rougek import RougeK

rk = RougeK()
hypo = "This is a generated summary."
kws = ["summary"]

result = rk(hypo, kws)
print(f"ROUGE-K: {result}.")
```


### From CLI

Of course, this package gives you an option as a CLI command so that you don't need to touch any python scripts.

By running the following command, you get an avg of ROUGE-K scores for your summaries.

```sh
rougek evaluate /path/to/target.hypo /path/to/kws.jsonl
```

You can also evaluate multiple `.hypo` files in a directory by following,

```sh
rougek evaluate_dir /dir/with/hypofiles /path/to/kws.jsonl
```

target hypo files need to have an extension of `.hypo` to be considered.
