from pandas.api.types import CategoricalDtype

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def to_categorical(series):

    t = pd.CategoricalDtype(categories=['A00-A04', 'A05-A14', 'A15-A34', 'A35-A59', 'A60-A79',
                  'A80+'], ordered=True)
    final = pd.Series(series, dtype=t)
    #print(series)
    return final


if __name__ == "__main__":

    df = pd.read_csv("data/RKI_COVID.csv", usecols=["AgeGroup"])
    ser = to_categorical(df["AgeGroup"])
    print(ser)
