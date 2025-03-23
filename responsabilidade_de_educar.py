import matplotlib.pyplot as plt

# Dados
categorias = [
    "Acho que sim, mas também é responsabilidade do consumidor",
    "Sim, totalmente",
    "Não, cada um deve cuidar disso por conta própria",
    "Não sei"
]

contagem = [27, 20, 5, 1]
porcentagens = [51, 38, 9, 2]
cores = ["#8BC34A", "#4CAF50", "#F44336", "#BDBDBD"]

# Figura e eixos
fig, ax = plt.subplots(figsize=(8, 8))

# Gráfico pizza
wedges, texts, autotexts = ax.pie(
    porcentagens,
    labels=[f'{porc}%' for porc in porcentagens],
    colors=cores,
    autopct='%1.0f%%',
    startangle=90,
    textprops={'fontsize': 12, 'color': 'white', 'weight': 'bold'},
    wedgeprops={'edgecolor': 'white'}
)

# Legenda posicionada abaixo
ax.legend(
    wedges,
    [f'{cat} ({porc}%)' for cat, porc in zip(categorias, porcentagens)],
    title="Categorias",
    loc="upper center",
    bbox_to_anchor=(0.5, -0.05),
    fontsize=10,
    title_fontsize=12,
    ncol=1,
    frameon=False
)

# Título
plt.title("Você acredita que as marcas devem educar consumidores\nsobre sustentabilidade?", fontsize=15)

# Aspecto circular
ax.axis('equal')

# Ajuste manual das margens para legenda ficar bem posicionada
plt.subplots_adjust(bottom=0.25)

plt.show()
