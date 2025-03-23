import matplotlib.pyplot as plt
import seaborn as sns

# Dados
categorias = [
    "Muito importante",
    "Importante, mas não prioridade",
    "Não me importa muito",
    "Não é importante"
]

contagem = [25, 15, 8, 5]
cores = ["#4CAF50", "#8BC34A", "#FFC107", "#F44336"]

# Tamanho do gráfico
plt.figure(figsize=(12, 4))
sns.set_style("whitegrid")

# Loop para criar o pictograma começando em 1
for categoria, qtd, cor in zip(categorias, contagem, cores):
    plt.scatter(range(1, qtd + 1), [categoria]*qtd, color=cor, s=200, marker='o')

# Ajustes estéticos
plt.xlabel("Número de pessoas")
plt.title("Quão importante é para você que cosméticos tenham embalagens sustentáveis?")

# Alinhando última bolinha com número 25 e numerando conforme solicitado
plt.xlim(0, 26)
plt.xticks([1, 5, 10, 15, 20, 25])

plt.tight_layout()
plt.grid(False)
sns.despine(left=True, bottom=True)

plt.show()
