import pandas as pd

from collections import Counter

def main_descriptive_statistics(dataframe):
    numeric_columns = ["IMDB_Rating", "Released_Year", "Runtime", "Meta_score", "No_of_Votes", "Gross", "Overview_len_words"]
    descriptive_table = dataframe[numeric_columns].describe().T.round(2)
    print(descriptive_table)
    return descriptive_table


def main_genres(dataframe):
    genre_counts = dataframe["Genre"].value_counts(dropna=False).to_frame("count")
    print(genre_counts)
    return genre_counts


def main_directors(dataframe):
    main_directors = dataframe["Director"].value_counts().to_frame("count")
    main_directors.to_csv("../NewDocuments/directors_count.csv")
    print(main_directors)
    return main_directors


def best_blind_pick(dataframe):
    dataframe["Score"] = dataframe["No_of_Votes"] * dataframe["IMDB_Rating"]
    best_combo = dataframe.loc[dataframe["Score"].idxmax()]
    print(best_combo["Series_Title"])
    return best_combo


def actors_in_bigest_gross(dataframe, quantile=0.9):
    gross_threshold = dataframe["Gross"].quantile(quantile)
    top_gross = dataframe[dataframe["Gross"] >= gross_threshold]

    actors_columns = ["Star1", "Star2", "Star3", "Star4"]
    actors_list = top_gross[actors_columns].values.flatten()
    actors_list = [a for a in actors_list if pd.notna(a)]
    actor_counts = Counter(actors_list)

    top_actors = pd.DataFrame(actor_counts.most_common(10), columns=["Actor", "Count"])
    top_actors.to_csv("top_actors.csv")
    print(top_actors)

def genres_in_biggest_gross(dataframe, quantile=0.9):
    gross_threshold = dataframe["Gross"].quantile(quantile)
    top_gross = dataframe[dataframe["Gross"] >= gross_threshold]

    genre_list = top_gross["Genre"]
    genre_list = [g for g in genre_list if pd.notna(g)]
    genre_counts = Counter(genre_list)

    top_genres = pd.DataFrame(genre_counts.most_common(10), columns=["Genre", "Count"])
    top_genres.to_csv("../NewDocuments/top_genres.csv")
    print(top_genres)

