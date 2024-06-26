import pandas as pd
import polars as pl

def process_data_hostel():
    df = pd.read_csv("data/hostel.csv", sep=";", dtype={"CODE POSTAL": str})

    df = df[df["TYPOLOGIE ÉTABLISSEMENT"] == "HÔTEL DE TOURISME"].reset_index(drop=True)

    df["KEY"] = df["ADRESSE"].str.lower() + " " + df["CODE POSTAL"]

    df["DEP"] = df["CODE POSTAL"].str[:2]

    pl_df = pl.from_pandas(df)

    return pl_df

pl_df = process_data_hostel()
print(pl_df.head())