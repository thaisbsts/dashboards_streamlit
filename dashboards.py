import pandas as pd
import streamlit as st
import plotly.express as px

# adicionando o título e uma descrição
st.title(':green[Dashboards] - Análise de Dados :rocket:')
st.text("Este trabalho utiliza um conjunto de dados de músicas do Spotify, contido em um \narquivo CSV, que inclui várias métricas como número de streams, nomes dos artistas,\nposições nas paradas e outras informações relevantes. O objetivo do estudo \nfoi compreender melhor as tendências de popularidade das músicas, identificar \npadrões sobre quais músicas e artistas dominam as paradas e analisar como \ndiferentes fatores influenciam o sucesso de uma música.")

df = pd.read_excel("testeVS.xlsx")

# Gráfico de barras das cinco músicas mais populares
st.subheader('Melhores cinco músicas (streams): ')
songs_spotify_desc = df.sort_values(by='streams', ascending=False)
df_head = songs_spotify_desc.head()
fig_bar = px.bar(df_head, x='track_name', y='streams')
st.plotly_chart(fig_bar)

# Segundo gráfico
st.subheader("Quantidade de streams por tom: ")
streams_agrupados = df.groupby('key')['streams'].sum()
fig = px.pie(streams_agrupados, values='streams', names=streams_agrupados.index)
st.plotly_chart(fig)

# Terceiro gráfico
st.subheader('Evolução dos streams ao longo dos meses (2022): ')
songs_spotify_2022 = df.loc[df['released_year'] == 2022]
soma_streams_por_mes = songs_spotify_2022.groupby('released_month')['streams'].sum()
fig_bar = px.bar(soma_streams_por_mes, x=soma_streams_por_mes.index, y='streams')
st.plotly_chart(fig_bar)

st.subheader('Quantidade de músicas por data de lançamento: ')
songs_ano_lancamento = df['released_year'].value_counts()
songs_ano_lancamento = songs_ano_lancamento.sort_index() # Ordenando os anos
fig_bar = px.bar(x=songs_ano_lancamento.index, y=songs_ano_lancamento.values, color_discrete_sequence=['red'])
fig_bar.update_layout(
    xaxis_title="Ano de lançamento",
    yaxis_title="Quantidade de Músicas"
)
st.plotly_chart(fig_bar)

# Quarto gráfico
st.subheader('Quantidade de playlists em cada plataforma: ')
in_spotify_playlists = df['in_spotify_playlists'].sum()
in_deezer_playlists = df['in_deezer_playlists'].sum()
in_apple_playlists = df['in_apple_playlists'].sum()

labels = ['Spotify', 'Deezer', 'Apple Music']
sizes = [in_spotify_playlists, in_deezer_playlists, in_apple_playlists]

fig = px.pie(values=sizes, names=labels)
st.plotly_chart(fig)

# Quinto gráfico
st.subheader('Charts por plataforma: ')
in_spotify_charts = df['in_spotify_charts'].sum()
in_deezer_charts = df['in_deezer_charts'].sum()
in_apple_charts = df['in_apple_charts'].sum()

labels = ['Spotify', 'Deezer', 'Apple Music']
sizes = [in_spotify_charts, in_deezer_charts, in_apple_charts]

fig = px.pie(values=sizes, names=labels)
st.plotly_chart(fig)

# Sexto gráfico
st.subheader('Quantidade de músicas por quantidade de artistas: ')
songs_qntd_artistas = df['artist_count'].value_counts()

songs_qntd_artistas = songs_qntd_artistas.sort_index()
fig = px.pie(values=songs_qntd_artistas.values, names=songs_qntd_artistas.index)
st.plotly_chart(fig)

# Sétimo gráfico
st.subheader('Quantidade de músicas por escala: ')
songs_spotify_escala_maior = df[df['mode'] == 'Major']
songs_spotify_escala_menor = df[df['mode'] == 'Minor']

maior_count = len(songs_spotify_escala_maior)
menor_count = len(songs_spotify_escala_menor)

labels = ["Minor", "Major"]
sizes = [menor_count, maior_count]
fig = px.pie(values=sizes, names=labels)
st.plotly_chart(fig)