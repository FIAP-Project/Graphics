import matplotlib.pyplot as plt

# Dados da pesquisa
categorias = [
    "Sim, várias vezes",
    "Sim, algumas vezes",
    "Não, nunca",
    "Não tenho certeza"
]

contagem = [7, 15, 20, 11]
porcentagens = [13, 28, 38, 21]
cores = ["#4CAF50", "#8BC34A", "#F44336", "#FFC107"]

# Gráfico de rosca
plt.figure(figsize=(7, 7))

wedges, texts, autotexts = plt.pie(
    contagem,
    labels=categorias,
    autopct='%1.0f%%',
    startangle=140,
    colors=cores,
    wedgeprops=dict(width=0.4),
    pctdistance=0.8,
)

# Título central
plt.title("Você já escolheu não comprar um cosmético por conter\ningredientes prejudiciais ao meio ambiente?", fontsize=14)

# Estética
for autotext in autotexts:
    autotext.set_fontsize(12)
    autotext.set_color('white')

plt.tight_layout()
plt.show()
