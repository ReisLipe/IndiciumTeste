# Resposta Indicium - Cientista de Dados
Este projeto foi desenvolvido como parte do processo seletivo do programa
Lighthouse da Indicium. O objetivo é realizar uma análise completa de dados
cinematográficos do IMDB para orientar o estúdio fictício "PProductions" sobre
qual tipo de filme deve ser o próximo a ser desenvolvido.

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
Prever a nota do IMDB é um problema de **regressão**. Para descobrir qual o
melhor modelo e quais seus prós e contras, testei dois modelos: **Regressão Linear** 
e **Random Forest**, o resultado obtido geramente é o seguinte:

Modelo: Linear Regression
RMSE: 0.2084
MAE: 0.1688
R2: 0.3383

Modelo: Random Forest
RMSE: 0.1936
MAE: 0.1477
R2: 0.4288

Para o filme `The Shawshank Redemption`, a previsão obtida por cada modelo é a
seguinte:

Linear Regression: 9.25
Random Forest: 8.79


