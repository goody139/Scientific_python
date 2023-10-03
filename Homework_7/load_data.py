import pandas as pd
import numpy as np
import pandas.core.dtypes.dtypes


def load_data():

    # load 2 RKI files 
    #countries = pd.read_csv (r'data\RKI_Counties.csv')
    countries = pd.read_csv("data/RKI_Counties.csv")
    #covid = pd.read_csv (r'data\RKI_COVID.csv')
    covid = pd.read_csv ('data/RKI_COVID.csv')

    covid = covid.astype({"ReportingDate": "datetime64[ns]"})

    #print(covid)


    # all columns from the RKI_COVID19 DataFrame plus the county column from RKI_Counties
    countries = countries.rename(columns={"RS": "IdCounty"})
    merged = pd.merge(covid,countries, on='IdCounty',how='left', indicator="left_only")

    list_covid = list(covid)
    list_merged = list(merged)
    for x in list_merged: 
        if x not in list_covid and x != "ReportingDate" and x != "county": 
            merged = merged.drop(x, axis=1)

    merged = merged.astype({"ReportingDate": "datetime64[ns]"})
    merged = merged.set_index('ReportingDate')
    merged = merged.sort_index(axis = "index")
    merged = merged.drop("AgeGroup2", axis=1)
    merged = merged.loc[:, ~merged.columns.str.contains('^Unnamed')]
    
    merged.index = pd.to_datetime(merged.index)
    #merged = pandas.to_datetime(merged, unit="ns")

    # should be (,7)
    #print(merged.shape)
    print(merged.dtypes)
    return merged 

if __name__ == "__main__":

    df = load_data()
    print(df)
