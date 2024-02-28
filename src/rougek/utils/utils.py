import numpy as np

def avg(values: list) -> float:
    return np.mean(np.array(values))

def std(values: list) -> float:
    return np.std(np.array(values))
