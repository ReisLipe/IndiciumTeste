import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from data_frame import clear_movie


movie_for_test = {
    'Series_Title': 'The Shawshank Redemption',
    'Released_Year': '1994',
    'Certificate': 'A',
    'Runtime': '142 min',
    'Genre': 'Drama',
    'Overview': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
    'Meta_score': 80.0,
    'Director': 'Frank Darabont',
    'Star1': 'Tim Robbins',
    'Star2': 'Morgan Freeman',
    'Star3': 'Bob Gunton',
    'Star4': 'William Sadler',
    'No_of_Votes': 2343110,
    'Gross': '28,341,469'
}


def act(dataframe):
    test_pct = 0.2
    life_universe_everything_else = 42

    x, y, num_features, cat_features = preprocess_data(dataframe)
    preprocessor = build_processor(num_features, cat_features)

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=test_pct, random_state=life_universe_everything_else
    )

    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(
            n_estimators=200,
            random_state=life_universe_everything_else,
            n_jobs=-1
        )
    }

    trained_models = {}
    for name, model in models.items():
        pipeline = Pipeline(steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ])

        pipeline.fit(x_train, y_train)
        trained_models[name] = pipeline
        metrics = evaluate_model(pipeline, x_test, y_test)

        print(f"\nModelo: {name}")
        for metric, value in metrics.items():
            print(f"{metric}: {value:.4f}")

    movie_df = clear_movie(movie_for_test)
    for name, pipeline in trained_models.items():
        predicted_rating = pipeline.predict(movie_df)[0]
        print(f"{name}: {predicted_rating:.2f}")



def preprocess_data(dataframe):
    target = "IMDB_Rating"
    features =  ["Released_Year", "Runtime", "Meta_score", "No_of_Votes", "Gross", "Overview_len_char", "Overview_len_words", "Genre", "Certificate"]
    numeric_features = ["Released_Year", "Runtime", "Meta_score", "No_of_Votes", "Gross", "Overview_len_char", "Overview_len_words"]
    categorical_features = ["Genre", "Certificate"]

    x = dataframe[features]
    y = dataframe[target]

    return x, y, numeric_features, categorical_features


def build_processor(numeric_features, categorical_features):
    numeric_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features)
        ]
    )

    return preprocessor

def evaluate_model(model, x_test, y_test):
    predictions = model.predict(x_test)

    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    return {"RMSE": rmse, "MAE": mae, "R2": r2}