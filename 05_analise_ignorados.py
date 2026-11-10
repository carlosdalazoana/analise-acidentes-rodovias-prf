
import pandas as pd
from pathlib import Path

pasta = Path("Dados/Brutos")
arquivos = sorted(pasta.glob("datatran*.csv"))

bases = []

for arquivo in arquivos:
    df = pd.read_csv(
        arquivo,
        sep=";",
        encoding="latin1"
    )
    df["ano"] = arquivo.stem[-4:]
    bases.append(df)

df = pd.concat(bases, ignore_index=True)

# Calcular divergência
df["soma_categorias"] = (
    df["mortos"]
    + df["feridos"]
    + df["ilesos"]
    + df["ignorados"]
)

df["diferenca"] = (
    df["pessoas"] - df["soma_categorias"]
)

df["inconsistente"] = df["diferenca"] != 0

print("=" * 60)
print("INVESTIGAÇÃO DA VARIÁVEL IGNORADOS")
print("=" * 60)

# 1. Presença de ignorados nos registros inconsistentes
print("\n1. REGISTROS INCONSISTENTES")

grupo = df.groupby("inconsistente").agg(
    ocorrencias=("id", "count"),
    media_ignorados=("ignorados", "mean"),
    registros_com_ignorados=(
        "ignorados",
        lambda x: (x > 0).sum()
    )
)

grupo["percentual_com_ignorados"] = (
    grupo["registros_com_ignorados"]
    / grupo["ocorrencias"] * 100
).round(2)

print(grupo)

# 2. Distribuição de ignorados
print("\n2. DISTRIBUIÇÃO DE IGNORADOS")

print(
    df[df["inconsistente"]]
    ["ignorados"]
    .value_counts()
    .sort_index()
    .to_string()
)

# 3. Comparação por ano
print("\n3. INCONSISTÊNCIAS POR ANO")

print(
    df.groupby("ano")["inconsistente"]
    .agg(["sum", "count", "mean"])
)

# 4. Comparar tamanho da divergência
print("\n4. RELAÇÃO ENTRE DIVERGÊNCIA E IGNORADOS")

print(
    df[df["inconsistente"]]
    .groupby("ignorados")["diferenca"]
    .agg(["count", "mean"])
    .sort_values("count", ascending=False)
    .head(15)
)

print("\nINVESTIGAÇÃO CONCLUÍDA!")
