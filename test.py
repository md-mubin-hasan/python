import numpy as np
import pandas as pd

def run(random, /, *args, strict=False, **kwargs):
    ts = pd.Series(random(*args, **kwargs))
    A, B = np.log(ts.mean()), np.log(ts).mean()
    return A, B, A > B or not strict and np.abs(A - B) < 1e-9

size = 1
strict = False

print(run(np.random.lognormal, 10,  size=size, strict=strict)[-1])