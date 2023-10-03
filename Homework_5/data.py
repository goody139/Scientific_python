import pandas as pd

df = pd.read_csv("data/pokemon_no_duplicates.csv")
freqs_dataframe = df.groupby(["Type 1", "Type 2"])["Name"].count().unstack(fill_value=0)
freq_values = freqs_dataframe.values
freq_names = list(freqs_dataframe.index)
