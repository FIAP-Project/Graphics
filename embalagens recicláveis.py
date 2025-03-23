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
porcentagens = ["47%", "28%", "15%", "9%"]
cores = ["#4CAF50", "#8BC34A", "#FFC107", "#F44336"]

# Configuração da figura
plt.figure(figsize=(14, 5))
sns.set_style("whitegrid")

# Loop para criar o pictograma começando em 1
for categoria, qtd, cor, perc in zip(categorias, contagem, cores, porcentagens):
    plt.scatter(range(1, qtd + 1), [categoria]*qtd, color=cor, s=200, marker='o')
    # Adiciona a porcentagem no final das bolinhas
    plt.text(qtd + 0.5, categoria, perc, va='center', ha='left', fontsize=12, fontweight='bold')

# Ajustes estéticos
plt.xlabel("Número de pessoas")
plt.title("Quão importante é para você que cosméticos tenham embalagens sustentáveis?")

# Alinhando última bolinha com número 25 e numerando conforme solicitado
plt.xlim(0, 28)
plt.xticks([1, 5, 10, 15, 20, 25])

plt.tight_layout()
plt.grid(False)
sns.despine(left=True, bottom=True)

plt.show()
