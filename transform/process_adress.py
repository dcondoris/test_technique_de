import polars as pl

def process_data_adress():
    df = pl.read_csv("data/adresses-france.csv", separator=";", dtypes={"numero": pl.Utf8, "code_postal": pl.Utf8, "code_insee": pl.Utf8})

    df = df.fill_null(value="")

    col = df[["numero", "rep", "nom_voie", "code_postal"]].apply(lambda x: " ".join(x))

    col = col.with_columns(
        pl.col('map').str.replace(r"\s\s", " ")
    )

    col = col.with_columns(
        pl.col('map').str.to_lowercase()
    )

    df_clean = pl.concat([df, col], how="horizontal").rename({"map": "KEY"})

    return(df_clean.head())