import matplotlib.pyplot as plt
import seaborn as sns

# Dados da pesquisa
categorias = [
    "Sim, com certeza",
    "Não vejo isso como uma prioridade",
    "Seria bom, mas não vejo necessidade",
    "Não acho necessário"
]

contagem = [37, 7, 4, 4]
porcentagens = [71, 13, 8, 8]

cores = ["#4CAF50", "#FFC107", "#03A9F4", "#F44336"]

# Figura
plt.figure(figsize=(10, 5))
sns.set_style("whitegrid")

# Gráfico de barras horizontais
ax = sns.barplot(x=porcentagens, y=categorias, palette=cores, orient='h')

# Adicionando anotações (porcentagem e nº de pessoas)
for i, (valor, pessoas) in enumerate(zip(porcentagens, contagem)):
    ax.text(valor + 1, i, f"{valor}% ({pessoas} pessoas)", va='center', fontsize=12, color='black')

# Ajustes estéticos
plt.title("Você acredita que empresas devem divulgar informações claras\nsobre o impacto ambiental dos cosméticos?")
plt.xlabel("Porcentagem (%)")
plt.ylabel("")

plt.xlim(0, 85)
sns.despine(left=True, bottom=True)

plt.tight_layout()
plt.show()
