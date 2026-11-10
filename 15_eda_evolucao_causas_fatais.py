
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Caminhos
pasta_projeto = Path(__file__).parent
pasta_tratados = pasta_projeto / "Dados" / "Tratados"

arquivo = pasta_tratados / "acidentes_prf_2020_2025.parquet"

# 2. Carregar base
df = pd.read_parquet(arquivo)

# 3. Filtrar período de 2021 a 2025
df = df[df["ano"] >= 2021].copy()

print("=" * 65)
print("EDA - EVOLUÇÃO DAS CAUSAS FATAIS - PRF")
print("=" * 65)

# 4. Ranking das causas com mais mortes
ranking = (
    df.groupby("causa_acidente")["mortos"]
    .sum()
    .sort_values(ascending=False)
)

top_causas = ranking.head(5).index

print("\n1. TOP 5 CAUSAS COM MAIS MORTES")
print(ranking.head(5).to_string())

# 5. Evolução anual das mortes
evolucao = (
    df[df["causa_acidente"].isin(top_causas)]
    .groupby(["ano", "causa_acidente"])["mortos"]
    .sum()
    .unstack(fill_value=0)
)

print("\n2. EVOLUÇÃO ANUAL DAS MORTES")
print(evolucao.to_string())

# 6. Gráfico de evolução
plt.figure(figsize=(13, 7))

for causa in evolucao.columns:
    plt.plot(
        evolucao.index,
        evolucao[causa],
        marker="o",
        label=causa
    )

plt.title("Evolução das principais causas de mortes - PRF")
plt.xlabel("Ano")
plt.ylabel("Quantidade de mortes")
plt.xticks(evolucao.index)
plt.legend(fontsize=8)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(
    pasta_projeto / "eda_evolucao_causas_fatais.png",
    dpi=300
)

plt.show()

# 7. Salvar tabela
evolucao.to_csv(
    pasta_tratados / "evolucao_causas_fatais.csv",
    encoding="utf-8-sig"
)

print("\nANÁLISE CONCLUÍDA!")
print("Tabela e gráfico salvos com sucesso.")
