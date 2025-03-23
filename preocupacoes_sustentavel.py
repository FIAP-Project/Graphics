import matplotlib.pyplot as plt
import seaborn as sns

# Dados
categorias = [
    "Eficácia do produto",
    "Preço mais alto",
    "Certificações e comprovações da marca",
    "Disponibilidade no mercado",
    "Outros"
]

contagem = [34, 24, 21, 18, 3]
porcentagens = [34, 24, 21, 18, 3]
cores = ["#4CAF50", "#FFC107", "#03A9F4", "#8BC34A", "#BDBDBD"]

# Figura
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")

# Barras horizontais ordenadas por contagem
ax = sns.barplot(
    x=porcentagens,
    y=categorias,
    palette=cores,
    orient='h'
)

# Adicionar valores no final das barras
for i, (valor, cnt) in enumerate(zip(porcentagens, contagem)):
    ax.text(valor + 1, i, f"{valor}% ({cnt} pessoas)", va='center', fontsize=11)

# Ajustes visuais
plt.xlabel("Porcentagem (%)")
plt.ylabel("")
plt.title("Principais preocupações ao escolher um cosmético sustentável", fontsize=15)

plt.xlim(0, 45)
sns.despine(left=True, bottom=True)

plt.tight_layout()
plt.show()
