import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Dados com frequências (inclui porcentagem e quantidades)
dados = {
    "Conciência Ambiental (7%, 2)": 2,
    "Marcas (4%, 1)": 1,
    "Nível (4%, 1)": 1,
    "Natureza (7%, 2)": 2,
    "Disponibilidade (7%, 2)": 2,
    "Mercado (7%, 2)": 2,
    "Produto (15%, 4)": 4,
    "Cuidado (11%, 3)": 3,
    "Preço (52%, 14)": 14,
    "Impacto Ambiental (7%, 2)": 2,
    "Meio Ambiente (19%, 5)": 5,
    "Animais (7%, 2)": 2,
    "Parte (4%, 1)": 1,
    "Qualidade (22%, 6)": 6,
    "Consumidor (4%, 1)": 1,
    "Marca (11%, 3)": 3,
    "Concientização (4%, 1)": 1,
}

# Gerar WordCloud com palavras apenas na horizontal
wordcloud = WordCloud(
    width=1000,
    height=600,
    background_color='white',
    colormap='plasma',
    max_words=100,
    prefer_horizontal=1.0,  # Todas as palavras na horizontal
    min_font_size=10,
    font_path='C:/Windows/Fonts/Calibri.ttf',  # Ajuste o caminho conforme seu sistema operacional
    collocations=False,
    random_state=42
).generate_from_frequencies(dados)

# Exibir gráfico
plt.figure(figsize=(12, 8))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Motivos mencionados pelos participantes para usar cosméticos mais sustentáveis", fontsize=18, pad=20)
plt.show()
