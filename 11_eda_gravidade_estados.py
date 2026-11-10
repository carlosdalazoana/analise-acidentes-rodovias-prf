
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Carregar base
arquivo = Path(
    "Dados/Tratados/acidentes_prf_2020_2025.parquet"
)

df = pd.read_parquet(arquivo)

print("=" * 60)
print("EDA - GRAVIDADE DOS ACIDENTES POR ESTADO")
print("=" * 60)

# 2. Agrupar por estado
gravidade = df.groupby("uf").agg(
    acidentes=("id", "count"),
    acidentes_fatais=("possui_morte", "sum"),
    mortes=("mortos", "sum"),
    feridos_graves=("feridos_graves", "sum")
).reset_index()

# 3. Calcular indicadores
gravidade["percentual_acidentes_fatais"] = (
    gravidade["acidentes_fatais"]
    / gravidade["acidentes"] * 100
).round(2)

gravidade["mortes_por_100_acidentes"] = (
    gravidade["mortes"]
    / gravidade["acidentes"] * 100
).round(2)

# 4. Ranking de acidentes fatais
ranking = gravidade.sort_values(
    "percentual_acidentes_fatais",
    ascending=False
)

print("\n1. RANKING - PERCENTUAL DE ACIDENTES FATAIS")

print(
    ranking[
        ["uf", "acidentes", "acidentes_fatais",
         "percentual_acidentes_fatais"]
    ].to_string(index=False)
)

# 5. Ranking de mortes por 100 acidentes
print("\n2. RANKING - MORTES POR 100 ACIDENTES")

ranking_mortes = gravidade.sort_values(
    "mortes_por_100_acidentes",
    ascending=False
)

print(
    ranking_mortes[
        ["uf", "acidentes", "mortes",
         "mortes_por_100_acidentes"]
    ].to_string(index=False)
)

# 6. Gráfico - Top 10 percentual de acidentes fatais
top_fatais = ranking.head(10)

plt.figure(figsize=(11, 6))

plt.bar(
    top_fatais["uf"],
    top_fatais["percentual_acidentes_fatais"]
)

plt.title("Top 10 - Percentual de acidentes fatais por estado")
plt.xlabel("Estado")
plt.ylabel("Acidentes fatais (%)")
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

plt.savefig(
    "eda_gravidade_estados.png",
    dpi=300
)

plt.show()

# 7. Salvar resultados
pasta_saida = Path("Dados/Tratados")

gravidade.to_csv(
    pasta_saida / "gravidade_estados.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nANÁLISE CONCLUÍDA!")
