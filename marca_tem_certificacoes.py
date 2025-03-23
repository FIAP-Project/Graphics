import matplotlib.pyplot as plt
import seaborn as sns

# Dados
categorias = [
    "Nunca prestei atenção",
    "Às vezes, se a marca me agradar",
    "Sim, sempre",
    "Não sei o que são essas certificações"
]

contagem = [23, 14, 12, 4]
porcentagens = [43, 26, 23, 8]
cores = ["#F44336", "#FFC107", "#4CAF50", "#9E9E9E"]

# Figura
plt.figure(figsize=(10, 5))
sns.set_style("whitegrid")

# Criar barras horizontais
ax = sns.barplot(x=porcentagens, y=categorias, palette=cores, orient='h')

# Adicionando porcentagens e número de pessoas nas barras
for i, (valor, pessoas) in enumerate(zip(porcentagens, contagem)):
    ax.text(valor + 1, i, f"{valor}% ({pessoas} pessoas)", va='center', fontsize=11, fontweight='bold')

# Ajustes estéticos
plt.xlabel("Porcentagem (%)")
plt.ylabel("")
plt.title("Você costuma verificar certificações ambientais ou éticas\nnas marcas ao comprar cosméticos?", fontsize=14)

plt.xlim(0, 55)
sns.despine(left=True, bottom=True)
plt.tight_layout()
plt.show()
