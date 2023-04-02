import pandas as pd
import numpy as np
from scipy.stats import t
from scipy.stats import norm


chat_id = 474140315 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    a = 2 * x / 92**2
    x_bar = np.mean(a)
    s = np.std(a, ddof=1)
    se = s / np.sqrt(len(x))
    df = len(x) - 1
    t_value = t.ppf(1 - (1 - p) / 2, df)
    me = t_value * se
    ci = (x_bar - me, x_bar + me)
    return ci
