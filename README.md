# ROUGE-K


## Run extraction

Give an input file contains summarization data samples and a path to save extracted keywords.

Input data needs to be in jsonline format, each line is a dictionaly containing one data sample.

Each sample in input files need three information, (1) `source (List[str])`: List of sentences in source document, (2) `target (List[str])`: List of reference summaries, it can be a list with just one element (one sentence) if there is only one reference summary in your dataset, (3) `title (str)`: title of the source documents.

There is a sample data in `./tests/sample.jsonl`

```
rougek extract sample.jsonl output.jsonl
```

Resulting data (`output.jsonl` in the example above) is also a jsonline file, each line contains a list of keywords (`List[str]`) for one data sample.


## Run evaluation

### From python

You can evaluate your summaries by ROUGE-K in your python scripts as follows:

```py3
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

```bash
> rougek evaluate /path/to/target.hypo /path/to/kws.jsonl
```

You can also evaluate multiple `.hypo` files in a directory by following,

```bash
> rougek evaluate_dir /dir/with/hypofiles /path/to/kws.jsonl
```

target hypo files need to have an extension of `.hypo` to be considered.
