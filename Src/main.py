from data_frame import load_data, remove_missing_values, clear_data_frame
from plots import plot_imdb_rating_and_frequency, number_votes_and_imdb_rating, boxplot_genre_gross
from analysis import main_descriptive_statistics, main_genres, main_directors, best_blind_pick, actors_in_bigest_gross, genres_in_biggest_gross
from overview_inference import predict_genre_by_overview
from imdb_prediction import act

def get_clear_dataframe():
    csv_path = "../Documents/desafio_indicium_imdb.csv"
    raw_data_frame = load_data(csv_path)
    raw_data_frame = remove_missing_values(raw_data_frame, False)
    data_frame = clear_data_frame(raw_data_frame)

    print(data_frame.head())

    return data_frame

def main():
    df = get_clear_dataframe()
    
    # overview = "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."
    # predict_genre_by_overview(df, overview)

    act(df)


    


if __name__ == '__main__':
    main()