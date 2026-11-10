
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Caminhos
pasta_projeto = Path(__file__).parent
pasta_tratados = pasta_projeto / "Dados" / "Tratados"

arquivo = pasta_tratados / "acidentes_prf_2020_2025.parquet"

# 2. Carregar base
df = pd.read_parquet(arquivo)

print("=" * 60)
print("EDA - EVOLUÇÃO DAS CAUSAS DE ACIDENTES")
print("=" * 60)

# 3. Identificar as cinco principais causas
# Excluir 2020 da análise de causas
df = df[df["ano"] >= 2021].copy()
top_causas = (
    df.groupby("causa_acidente")
    .size()
    .nlargest(5)
    .index
)

# 4. Evolução anual das causas
evolucao = (
    df[df["causa_acidente"].isin(top_causas)]
    .groupby(["ano", "causa_acidente"])
    .size()
    .unstack(fill_value=0)
)

print("\n1. EVOLUÇÃO ANUAL DAS CINCO PRINCIPAIS CAUSAS")
print(evolucao.to_string())

# 5. Gráfico de evolução
plt.figure(figsize=(13, 7))

for causa in evolucao.columns:
    plt.plot(
        evolucao.index,
        evolucao[causa],
        marker="o",
        label=causa
    )

plt.title("Evolução das principais causas de acidentes - PRF")
plt.xlabel("Ano")
plt.ylabel("Quantidade de acidentes")
plt.xticks(evolucao.index)
plt.legend(fontsize=8)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(
    pasta_projeto / "eda_evolucao_causas.png",
    dpi=300
)

plt.show()

# 6. Salvar tabela
evolucao.to_csv(
    pasta_tratados / "evolucao_causas.csv",
    encoding="utf-8-sig"
)

print("\nANÁLISE CONCLUÍDA!")
print("Tabela e gráfico salvos com sucesso.")

