import re
import numpy as np
import pandas as pd

from pathlib import Path


# MARK: - Public Functions
def load_data(path):
    raw_data_frame = pd.read_csv(path)
    raw_data_frame.columns = [c.strip().replace(" ", "_") for c in raw_data_frame.columns]

    return raw_data_frame

def remove_missing_values(raw_data_frame, show_missing_info):
    missing = raw_data_frame.isna().sum().to_frame("missing")

    if show_missing_info:
        missing_percentage = (missing["missing"] / len(raw_data_frame) * 100)
        missing["percentage"] = missing_percentage.round(2)
        missing = missing.sort_values("missing", ascending=False)
        print(missing_info)

    return raw_data_frame

def clear_data_frame(raw_data_frame):
    data_frame = raw_data_frame.copy()

    data_frame["Released_Year"] = pd.to_numeric(data_frame["Released_Year"], errors="coerce")
    data_frame["Meta_score"] = pd.to_numeric(data_frame["Meta_score"], errors="coerce")
    data_frame["No_of_Votes"] = pd.to_numeric(data_frame["No_of_Votes"], errors="coerce")
    data_frame["IMDB_Rating"] = pd.to_numeric(data_frame["IMDB_Rating"], errors="coerce")

    data_frame["Runtime"] = data_frame["Runtime"].str.replace(" min", "", regex=False).astype(float)
    data_frame["Gross"] = data_frame["Gross"].str.replace(",", "", regex=False).astype(float)
    data_frame["Genre"] = data_frame["Genre"].str.split(",").str[0]

    data_frame["Overview_len_char"] = data_frame["Overview"].fillna("").apply(len)
    data_frame["Overview_len_words"] = data_frame["Overview"].fillna("").apply(lambda s: len(s.split()))

    clean_path = Path("../Documents/imdb_clean.csv")
    data_frame.to_csv(clean_path, index=False)
    
    return data_frame

def clear_movie(new_movie: dict) -> pd.DataFrame:
    new_movie["Runtime"] = float(new_movie["Runtime"].replace("min", "").strip())
    new_movie["Gross"] = float(new_movie["Gross"].replace(",", ""))
    new_movie["Released_Year"] = float(new_movie["Released_Year"])
    new_movie["Overview_len_char"] = len(new_movie["Overview"])
    new_movie["Overview_len_words"] = len(new_movie["Overview"].split())

    return pd.DataFrame([{
        "Released_Year": new_movie["Released_Year"],
        "Runtime": new_movie["Runtime"],
        "Meta_score": new_movie["Meta_score"],
        "No_of_Votes": new_movie["No_of_Votes"],
        "Gross": new_movie["Gross"],
        "Overview_len_char": new_movie["Overview_len_char"],
        "Overview_len_words": new_movie["Overview_len_words"],
        "Genre": new_movie["Genre"],
        "Certificate": new_movie["Certificate"]
    }])
