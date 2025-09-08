import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score


def predict_genre_by_overview(dataframe, overview):
    test_size = 0.2
    life_universe_everything_else = 42

    x_train, x_test, y_train, y_test = train_test_split(
        dataframe['Overview'], dataframe['Genre'], test_size=test_size, random_state=life_universe_everything_else
    )

    vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    x_train_tfidf = vectorizer.fit_transform(x_train)
    x_test_tfidf = vectorizer.transform(x_test)

    model = LogisticRegression(max_iter=200)
    model.fit(x_train_tfidf, y_train)

    y_pred = model.predict(x_test_tfidf)
    print("Acurácia:", accuracy_score(y_test, y_pred))
    print("\nRelatório de Classificação:\n", classification_report(y_test, y_pred))

    new_overview = [overview]
    new_vec = vectorizer.transform(new_overview)
    print("Gênero previsto:", model.predict(new_vec)[0])



