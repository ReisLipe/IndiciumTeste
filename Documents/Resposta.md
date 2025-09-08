# Resposta Indicium - Cientista de Dados
...

# 2a. Qual filme você recomendaria para uma pessoa que você não conhece?
Eu indicaria o filme com a maior nota acompanhado do maior público, isto é, com
o melhor desempenho na relação IMDB_rating X No_Votes. Quem melhor se encaixa
neste quesito é **The Dark Knight**, para tirar as dúvidas, basta utilizar a
função `number_votes_and_imdb_rating(dataframe)`.

# 2b. Quais são os principais fatores que estão relacionados com alta expectativa de faturamento de um filme?
Quando relacionamos a coluna de gênero (Genre) pela coluna de faturamento
(Gross) em um boxplot (`boxplot_genre_gross`) ou quando utilizamos a função de
análise `genres_in_biggest_gross`, podemos ver dos 100 filmes com um maior
faturamento, 70 deles se encaixam em Ação, Animação e Aventura. Porntanto, é
possível notar que o gênero do filme está intimamente ligado com o faturamento
do filme.

# 2c. Quais insights podem ser tirados com a coluna Overview? É possível inferir o gênero do filme a partir dessa coluna?
A coluna Overview é a sinopse do filme, portanto podemos tirar informações sobre
o contexto abordado pelo filme, incluindo o seu gênero. Portanto, é possível sim
inferir o gênero a partir da coluna overview, como exemplificado pela função
`predict_genre_by_overview`. 

# 3. Explique como você faria a previsão da nota do imdb a partir dos dados. Quais variáveis e/ou suas transformações você utilizou e por quê? Qual tipo de problema estamos resolvendo (regressão, classificação)? Qual modelo melhor se aproxima dos dados e quais seus prós e contras? Qual medida de performance do modelo foi escolhida e por quê?
Estamos resolvendo um problema de **regressão**, prevendo a nota do IMDB a
partir de variáveis como ano de lançamento, tempo de duração, metascore, número
de votos, bilheteria, além de variáveis categóricas como gênero e certificado.
Testamos diferentes modelos, sendo que métodos baseados em árvores (Random
Forest ou Gradient Boosting) se ajustam melhor aos dados por capturarem relações
não lineares. A métrica escolhida foi o RMSE, pois é mais sensível a grandes
erros e nos dá uma boa noção do desvio médio em relação à nota real.
