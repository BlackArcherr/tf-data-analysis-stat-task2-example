import pandas as pd
import numpy as np

import scipy.stats as stats

chat_id = 474140315

def solution(p: float, x: np.array) -> tuple:
    l = 2*(stats.erlang.ppf((1-p)/2, len(x), loc=0, scale=1/len(x)) + np.mean(x) - 1/2) / 92**2
    r = 2*(stats.erlang.ppf(1-(1-p)/2, len(x), loc=0, scale=1/len(x)) + np.mean(x) - 1/2) / 92**2
    return l, r
