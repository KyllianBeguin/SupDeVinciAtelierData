import requests
import os
import logging
import polars as pl

def init_loging():
    """Initialize logging"""
    logging.basicConfig(
        format='[%(levelname)s] %(asctime)s - %(message)s',
        level=logging.INFO,
        datefmt='%d-%b-%y %H:%M:%S'
    )
    return None

def download_data(raw_file="RawData.csv"):
    """download data from Open Data Rennes Metropole"""
    url = (
        "https://data.rennesmetropole.fr/api/explore/v2.1/catalog/dataset"
        "s/eco-counter-data/exports/csv?lang=fr&timezone=Europe%2FBerlin&"
        "use_labels=true&delimiter=%3B"
    )
    logging.info("Running downloading !")
    r = requests.get(url)
    with open(raw_file, 'wb') as f:
        f.write(r.content)
    logging.info("Complete ! Raw File located here: ./RawData.csv")
    return None

def read_data(raw_file="RawData.csv"):
    """Read Raw File"""
    logging.info(f"Reading raw file ./{raw_file}")
    counts = pl.read_csv(
        "./" + raw_file,
        separator=";",
        truncate_ragged_lines=True
    )
    os.remove(f"./{raw_file}")
    return counts
    
def transform_data(counts_raw):
    """Perform transformations on the dataset
    Transformations:
        - Unpack Date
        - Lower "name" column
        - Keep some columns
    """
    logging.info("Transforming raw data...")
    
    # Unpack Date
    cast_date = counts_raw.with_columns(
        pl.col("date").str.to_datetime().alias("datetime")
    )
    unpack_date = cast_date.with_columns([
        pl.col("datetime").dt.year().alias("year"),
        pl.col("datetime").dt.month().alias("month"),
        pl.col("datetime").dt.day().alias("day"),
        pl.col("datetime").dt.hour().alias("hour")
    ])
    logging.info("Done: Date unpacking.")
    
    # Lower "name" column
    lower_name = unpack_date.with_columns(
        pl.col("name").str.to_lowercase().alias("name_lower")
    )
    logging.info("Done: name lowering.")
    
    # Keep some clumns
    filtered  = lower_name.select(pl.col("datetime", "year", "month", "day", "hour", "counts", "name_lower"))
    logging.info("Done: columns filtering.")
    
    drop_nan = filtered.select(pl.col("counts").drop_nans())
    logging.info("Done: nans dropping")

    return drop_nan
    
def load_data(counts_clean):
    """Load data to a mysql database"""
    logging.info("Exporting Data...")
    
    table_name = "countsclean"
    database_name = "atelierdata"
    
    counts_clean.write_database(
        table_name=table_name,
        connection=f"mysql+mysqlconnector://root:supdevinci@127.0.0.1/{database_name}",
        if_table_exists="replace"
    )
    logging.info(f"Exported cleaned data to db={database_name} table={table_name}")
    return None

if __name__ == "__main__":
    init_loging()
    download_data()
    counts_raw = read_data()
    counts_clean = transform_data(counts_raw)
    load_data(counts_clean)
