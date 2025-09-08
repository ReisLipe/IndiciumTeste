import seaborn as sns
import matplotlib.pyplot as plt


def plot_imdb_rating_and_frequency(dataframe):
    plt.boxplot(dataframe["IMDB_Rating"].dropna())
    plt.title("Distribuição das notas do IMDB")
    plt.ylabel("IMDB Rating")
    plt.show()

def plot_imdb_rating_and_genre(dataframe):
    top8 = df["Main_Genre"].value_counts().head(8).index.tolist()
    subset = df[df["Main_Genre"].isin(top8)]
    
    plt.figure()
    subset.boxplot(column="IMDB_Rating", by="Main_Genre", rot=45)
    plt.suptitle("")
    plt.title("IMDB_Rating por Main_Genre (Top 8)")
    plt.xlabel("Main_Genre")
    plt.ylabel("IMDB_Rating")
    plt.tight_layout()
    plt.show()

def number_votes_and_imdb_rating(dataframe):
    plt.figure()
    plt.scatter(dataframe["No_of_Votes"], dataframe["IMDB_Rating"])
    plt.title("Num. Votos vs Notas IMDB")
    plt.xlabel("Num. Votos (Milhão)")
    plt.ylabel("Notas IMDB")
    plt.tight_layout()
    plt.show()

def boxplot_genre_gross(dataframe):
    plt.figure(figsize=(14, 7))
    sns.boxplot(data=dataframe, x="Genre", y="Gross")
    plt.xticks(rotation=45, ha="right")
    plt.title("Distribuição do Gross por Gênero")
    plt.xlabel("Gênero")
    plt.ylabel("Faturamento (Gross)")
    plt.tight_layout()
    plt.show()