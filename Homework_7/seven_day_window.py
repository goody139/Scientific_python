from load_data import load_data

import pandas as pd
import numpy as np


def seven_day_window(df):

    """
    df = df.drop("AgeGroup", axis=1)
    df = df.drop("Sex", axis=1)
    df = df.drop("county", axis=1)
    df = df.drop("IdCounty", axis=1)
    df = df.shift(1, freq="D")

    #df = df.rolling(8).sum()
    #df = df[df['#Cases'].notna()]

    df = df.groupby(df.index.date).count()
    df.index = pd.to_datetime(df.index)
    df.index.name = "ReportingDate"
    df = df.astype({"#Cases": "float64"})
    #df.index.freq = "D"

    #df_n = df.head(227)
    #should have 227 rows , 3 columns

    return df """

    resampled = df.resample("1D").sum()
    resampled = resampled.drop("IdCounty", axis=1)
    window = resampled.rolling(7).sum()
    window.index = window.index.shift(1)
    return window



if __name__ == "__main__":

    df = load_data()
    weekly_window = seven_day_window(df)
    print(weekly_window)

