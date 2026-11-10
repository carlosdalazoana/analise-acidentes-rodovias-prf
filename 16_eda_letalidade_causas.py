
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# 1. Caminhos
pasta_projeto = Path(__file__).parent
arquivo_dados = (
    pasta_projeto / "Dados" / "Tratados" / "acidentes_prf_2020_2025.parquet"
)

# 2. Carregar dados
df = pd.read_parquet(arquivo_dados)

# Excluir 2020
df = df[df["ano"] >= 2021].copy()

print("=" * 65)
print("EDA - LETALIDADE DAS CAUSAS DE ACIDENTES - PRF")
print("=" * 65)

# 3. Agrupar acidentes por causa
analise = (
    df.groupby("causa_acidente")
    .agg(
        acidentes=("id", "count"),
        acidentes_fatais=("possui_morte", "sum"),
        mortes=("mortos", "sum")
    )
    .reset_index()
)

# 4. Calcular indicadores
analise["percentual_fatalidade"] = (
    analise["acidentes_fatais"] / analise["acidentes"] * 100
)

analise["mortes_por_100_acidentes"] = (
    analise["mortes"] / analise["acidentes"] * 100
)

# 5. Ordenar por percentual de fatalidade
ranking = analise.sort_values(
    "percentual_fatalidade",
    ascending=False
)

print("\n1. TOP 15 CAUSAS COM MAIOR PERCENTUAL DE ACIDENTES FATAIS")

print(
    ranking.head(15).round(2).to_string(index=False)
)

# 6. Ordenar por mortes por 100 acidentes
ranking_mortes = analise.sort_values(
    "mortes_por_100_acidentes",
    ascending=False
)

print("\n2. TOP 15 CAUSAS COM MAIS MORTES POR 100 ACIDENTES")

print(
    ranking_mortes.head(15).round(2).to_string(index=False)
)

# 7. Salvar resultados
pasta_tratados = pasta_projeto / "Dados" / "Tratados"

ranking.to_csv(
    pasta_tratados / "letalidade_causas.csv",
    index=False,
    encoding="utf-8-sig"
)

# 8. Gráfico - percentual de acidentes fatais
top15 = ranking.head(15).sort_values(
    "percentual_fatalidade"
)

plt.figure(figsize=(12, 8))

plt.barh(
    top15["causa_acidente"],
    top15["percentual_fatalidade"]
)

plt.title("Top 15 causas com maior percentual de acidentes fatais - PRF")
plt.xlabel("Acidentes fatais (%)")
plt.ylabel("Causa do acidente")
plt.tight_layout()

plt.savefig(
    pasta_projeto / "eda_letalidade_causas.png",
    dpi=300
)

plt.show()

print("\nANÁLISE CONCLUÍDA!")
print("Tabela e gráfico salvos com sucesso.")
