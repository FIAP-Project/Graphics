import matplotlib.pyplot as plt
import seaborn as sns

# Dados
categorias = [
    "Um pouco disposto(a)",
    "Totalmente disposto(a)",
    "Não sei, depende do preço",
    "Não disposto(a)"
]

contagem = [23, 16, 9, 5]
porcentagens = [43, 30, 17, 9]
cores = ["#8BC34A", "#4CAF50", "#FFC107", "#F44336"]

# Figura
plt.figure(figsize=(9, 6))
sns.set_style("whitegrid")

# Criar gráfico de barras verticais
ax = sns.barplot(x=categorias, y=porcentagens, palette=cores)

# Adicionando porcentagens acima das barras
for i, (porcent, pessoas) in enumerate(zip(porcentagens, contagem)):
    ax.text(i, porcent + 1, f"{porcent}% ({pessoas} pessoas)",
            ha='center', fontsize=11, fontweight='bold')

# Ajustes
plt.ylim(0, 55)
plt.ylabel("Porcentagem (%)")
plt.xlabel("")
plt.title("Quão disposto(a) estaria a pagar mais por um cosmético\nambientalmente sustentável?", fontsize=14)

sns.despine(left=True, bottom=True)
plt.tight_layout()
plt.show()
