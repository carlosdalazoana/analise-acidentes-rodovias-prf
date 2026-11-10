
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Carregar base tratada
arquivo = Path(
    "Dados/Tratados/acidentes_prf_2020_2025.parquet"
)

df = pd.read_parquet(arquivo)

print("=" * 60)
print("EDA - PRINCIPAIS CAUSAS DOS ACIDENTES")
print("=" * 60)

# 2. Verificar valores ausentes
print("\n1. VALORES AUSENTES")
print(df["causa_acidente"].isna().sum())

# 3. Agrupar por causa
causas = df.groupby("causa_acidente").agg(
    acidentes=("id", "count"),
    mortes=("mortos", "sum"),
    acidentes_fatais=("possui_morte", "sum"),
    feridos=("feridos", "sum")
).reset_index()

# 4. Calcular indicadores
causas["participacao_acidentes_%"] = (
    causas["acidentes"] / len(df) * 100
).round(2)

causas["participacao_mortes_%"] = (
    causas["mortes"] / df["mortos"].sum() * 100
).round(2)

causas["percentual_acidentes_fatais"] = (
    causas["acidentes_fatais"]
    / causas["acidentes"] * 100
).round(2)

causas["mortes_por_100_acidentes"] = (
    causas["mortes"]
    / causas["acidentes"] * 100
).round(2)

# 5. Ranking por quantidade de acidentes
ranking_acidentes = causas.sort_values(
    "acidentes",
    ascending=False
)

print("\n2. RANKING DAS 15 PRINCIPAIS CAUSAS")

print(
    ranking_acidentes[
        ["causa_acidente", "acidentes",
         "participacao_acidentes_%"]
    ].head(15).to_string(index=False)
)

# 6. Ranking por quantidade de mortes
ranking_mortes = causas.sort_values(
    "mortes",
    ascending=False
)

print("\n3. TOP 15 CAUSAS COM MAIS MORTES")

print(
    ranking_mortes[
        ["causa_acidente", "acidentes", "mortes",
         "percentual_acidentes_fatais",
         "mortes_por_100_acidentes"]
    ].head(15).to_string(index=False)
)

# 7. Gráfico das 10 principais causas por acidentes
top_acidentes = ranking_acidentes.head(10).sort_values(
    "acidentes"
)

plt.figure(figsize=(12, 7))

plt.barh(
    top_acidentes["causa_acidente"],
    top_acidentes["acidentes"]
)

plt.title("Top 10 causas com mais acidentes - PRF")
plt.xlabel("Quantidade de acidentes")
plt.ylabel("Causa")
plt.grid(axis="x", alpha=0.3)

plt.tight_layout()

plt.savefig(
    "eda_top10_causas_acidentes.png",
    dpi=300
)

plt.show()

# 8. Gráfico das 10 causas com mais mortes
top_mortes = ranking_mortes.head(10).sort_values(
    "mortes"
)

plt.figure(figsize=(12, 7))

plt.barh(
    top_mortes["causa_acidente"],
    top_mortes["mortes"]
)

plt.title("Top 10 causas com mais mortes - PRF")
plt.xlabel("Quantidade de mortes")
plt.ylabel("Causa")
plt.grid(axis="x", alpha=0.3)

plt.tight_layout()

plt.savefig(
    "eda_top10_causas_mortes.png",
    dpi=300
)

plt.show()

# 9. Salvar resultados
pasta_saida = Path("Dados/Tratados")

causas.to_csv(
    pasta_saida / "analise_causas.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nANÁLISE CONCLUÍDA!")
print("Tabela e gráficos salvos com sucesso.")
