
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# 1. Caminhos
pasta_projeto = Path(__file__).parent

arquivo_dados = (
    pasta_projeto
    / "Dados"
    / "Tratados"
    / "acidentes_prf_2020_2025.parquet"
)

# 2. Carregar dados
df = pd.read_parquet(arquivo_dados)

# Excluir 2020
df = df[df["ano"] >= 2021].copy()

print("=" * 65)
print("EDA - DISTRIBUIÇÃO TEMPORAL DOS ACIDENTES - PRF")
print("=" * 65)

# 3. Análise por mês
print("\n1. ACIDENTES POR MÊS")

nomes_meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

por_mes = (
    df.groupby("mes")
    .agg(
        acidentes=("id", "count"),
        mortes=("mortos", "sum")
    )
    .reindex(range(1, 13), fill_value=0)
)

por_mes.index = [
    nomes_meses[m] for m in por_mes.index
]

print(por_mes.to_string())


# 4. Análise por dia da semana
print("\n2. ACIDENTES POR DIA DA SEMANA")

por_dia = (
    df.groupby("dia_semana")
    .agg(
        acidentes=("id", "count"),
        mortes=("mortos", "sum")
    )
)

print(por_dia.sort_values(
    "acidentes", ascending=False
).to_string())

# 5. Análise por horário
print("\n3. ACIDENTES POR HORA")

df["hora"] = pd.to_numeric(
    df["horario"].str[:2],
    errors="coerce"
)

por_hora = (
    df.groupby("hora")
    .agg(
        acidentes=("id", "count"),
        mortes=("mortos", "sum")
    )
    .reindex(range(24), fill_value=0)
)

print(por_hora.to_string())

# 6. Análise por fase do dia
print("\n4. ACIDENTES POR FASE DO DIA")

por_fase = (
    df.groupby("fase_dia")
    .agg(
        acidentes=("id", "count"),
        mortes=("mortos", "sum")
    )
    .sort_values("acidentes", ascending=False)
)

print(por_fase.to_string())

# 7. Gráfico de acidentes por mês
plt.figure(figsize=(12, 6))

plt.bar(por_mes.index, por_mes["acidentes"])

plt.title("Acidentes por mês - PRF (2021-2025)")
plt.xlabel("Mês")
plt.ylabel("Quantidade de acidentes")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    pasta_projeto / "eda_acidentes_mes.png",
    dpi=300
)

plt.show()

# 8. Gráfico por dia da semana
plt.figure(figsize=(11, 6))

dia_ordenado = por_dia.sort_values("acidentes")

plt.barh(
    dia_ordenado.index,
    dia_ordenado["acidentes"]
)

plt.title("Acidentes por dia da semana - PRF (2021-2025)")
plt.xlabel("Quantidade de acidentes")
plt.ylabel("Dia da semana")

plt.tight_layout()

plt.savefig(
    pasta_projeto / "eda_acidentes_dia_semana.png",
    dpi=300
)

plt.show()

# 9. Gráfico por hora
plt.figure(figsize=(12, 6))

plt.plot(
    por_hora.index,
    por_hora["acidentes"],
    marker="o"
)

plt.title("Distribuição de acidentes por hora - PRF (2021-2025)")
plt.xlabel("Hora do dia")
plt.ylabel("Quantidade de acidentes")
plt.xticks(range(24))
plt.grid(True)

plt.tight_layout()

plt.savefig(
    pasta_projeto / "eda_acidentes_hora.png",
    dpi=300
)

plt.show()

# 10. Gráfico por fase do dia
plt.figure(figsize=(10, 6))

plt.bar(
    por_fase.index,
    por_fase["acidentes"]
)

plt.title("Acidentes por fase do dia - PRF (2021-2025)")
plt.xlabel("Fase do dia")
plt.ylabel("Quantidade de acidentes")
plt.xticks(rotation=25)

plt.tight_layout()

plt.savefig(
    pasta_projeto / "eda_acidentes_fase_dia.png",
    dpi=300
)

plt.show()

# 11. Salvar tabelas
pasta_tratados = pasta_projeto / "Dados" / "Tratados"

por_mes.to_csv(
    pasta_tratados / "acidentes_por_mes.csv",
    encoding="utf-8-sig"
)

por_dia.to_csv(
    pasta_tratados / "acidentes_por_dia_semana.csv",
    encoding="utf-8-sig"
)

por_hora.to_csv(
    pasta_tratados / "acidentes_por_hora.csv",
    encoding="utf-8-sig"
)

por_fase.to_csv(
    pasta_tratados / "acidentes_por_fase_dia.csv",
    encoding="utf-8-sig"
)

print("\n" + "=" * 65)
print("ANÁLISE TEMPORAL CONCLUÍDA!")
print("Tabelas e gráficos salvos com sucesso.")
print("=" * 65)
