
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Carregar base tratada
arquivo = Path(
    "Dados/Tratados/acidentes_prf_2020_2025.parquet"
)

df = pd.read_parquet(arquivo)

print("=" * 60)
print("EDA - DISTRIBUICAO DE ACIDENTES POR ESTADO")
print("=" * 60)

# 2. Agrupar por estado
analise_uf = df.groupby("uf").agg(
    acidentes=("id", "count"),
    mortes=("mortos", "sum"),
    acidentes_fatais=("possui_morte", "sum"),
    feridos=("feridos", "sum")
).reset_index()

# 3. Calcular participação percentual
total_acidentes = analise_uf["acidentes"].sum()
total_mortes = analise_uf["mortes"].sum()

analise_uf["participacao_acidentes_%"] = (
    analise_uf["acidentes"] / total_acidentes * 100
).round(2)

analise_uf["participacao_mortes_%"] = (
    analise_uf["mortes"] / total_mortes * 100
).round(2)

# 4. Ordenar por quantidade de acidentes
analise_uf = analise_uf.sort_values(
    "acidentes",
    ascending=False
)

print("\n1. RANKING DE ACIDENTES POR ESTADO")

print(
    analise_uf[
        ["uf", "acidentes", "participacao_acidentes_%"]
    ].to_string(index=False)
)

# 5. Ranking de mortes
print("\n2. RANKING DE MORTES POR ESTADO")

print(
    analise_uf.sort_values(
        "mortes",
        ascending=False
    )[
        ["uf", "mortes", "participacao_mortes_%"]
    ].to_string(index=False)
)

# 6. Gráfico dos 10 estados com mais acidentes
top_acidentes = analise_uf.head(10)

plt.figure(figsize=(11, 6))

plt.bar(
    top_acidentes["uf"],
    top_acidentes["acidentes"]
)

plt.title("Top 10 estados com mais acidentes - PRF")
plt.xlabel("Estado")
plt.ylabel("Quantidade de acidentes")
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

plt.savefig(
    "eda_top10_acidentes_uf.png",
    dpi=300
)

plt.show()

# 7. Gráfico dos 10 estados com mais mortes
top_mortes = analise_uf.nlargest(10, "mortes")

plt.figure(figsize=(11, 6))

plt.bar(
    top_mortes["uf"],
    top_mortes["mortes"]
)

plt.title("Top 10 estados com mais mortes - PRF")
plt.xlabel("Estado")
plt.ylabel("Quantidade de mortes")
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

plt.savefig(
    "eda_top10_mortes_uf.png",
    dpi=300
)

plt.show()

# 8. Salvar resultados
pasta_saida = Path("Dados/Tratados")

analise_uf.to_csv(
    pasta_saida / "distribuicao_estados.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nANÁLISE CONCLUÍDA!")
print("Tabela e gráficos gerados.")
