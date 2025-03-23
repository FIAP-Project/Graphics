import matplotlib.pyplot as plt

# Dados
categorias = [
    "Qualidade do produto",
    "Preço",
    "Compromisso ambiental ou ético",
    "Popularidade ou recomendação"
]

contagem = [36, 11, 4, 2]
porcentagens = [68, 21, 8, 4]
cores = ["#4CAF50", "#FFC107", "#03A9F4", "#9E9E9E"]

# Figura
plt.figure(figsize=(10, 5))

# Linhas horizontais
plt.hlines(y=categorias, xmin=0, xmax=porcentagens, color='gray', linewidth=2)

# Pontos (pirulitos)
plt.scatter(porcentagens, categorias, color=cores, s=250)

# Adicionar porcentagens e número de pessoas
for i, (pct, cnt) in enumerate(zip(porcentagens, contagem)):
    plt.text(pct + 1, i, f"{pct}% ({cnt} pessoas)", fontsize=11, va='center')

# Ajustes
plt.title("Qual fator mais influencia sua decisão de compra de cosméticos?", fontsize=14)
plt.xlabel("Porcentagem (%)")
plt.xlim(0, 80)

plt.grid(False)
plt.tight_layout()
plt.show()
