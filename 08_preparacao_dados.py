
import pandas as pd
from pathlib import Path

# Caminhos
pasta_brutos = Path("Dados/Brutos")
pasta_tratados = Path("Dados/Tratados")

pasta_tratados.mkdir(parents=True, exist_ok=True)

arquivos = sorted(pasta_brutos.glob("datatran*.csv"))

# 1. Carregar e consolidar os arquivos
bases = []

for arquivo in arquivos:

    df = pd.read_csv(
        arquivo,
        sep=";",
        encoding="latin1"
    )

    bases.append(df)

df = pd.concat(bases, ignore_index=True)

print("BASE CONSOLIDADA:", df.shape)

# 2. Padronizar tipos de dados

df["id"] = df["id"].astype("Int64")

df["data_inversa"] = pd.to_datetime(
    df["data_inversa"],
    errors="coerce"
)

colunas_numericas = [
    "br", "pessoas", "mortos", "feridos",
    "feridos_leves", "feridos_graves",
    "ilesos", "ignorados", "veiculos"
]

for coluna in colunas_numericas:
    df[coluna] = pd.to_numeric(
        df[coluna],
        errors="coerce"
    )

# Coordenadas geográficas
for coluna in ["latitude", "longitude"]:
    df[coluna] = pd.to_numeric(
        df[coluna].astype(str).str.replace(
            ",", ".", regex=False
        ),
        errors="coerce"
    )

# Quilometragem
df["km"] = pd.to_numeric(
    df["km"].astype(str).str.replace(
        ",", ".", regex=False
    ),
    errors="coerce"
)

# 3. Criar variáveis temporais
df["ano"] = df["data_inversa"].dt.year
df["mes"] = df["data_inversa"].dt.month
df["nome_mes"] = df["data_inversa"].dt.month_name()

df["dia"] = df["data_inversa"].dt.day

# 4. Criar indicador de gravidade
df["possui_morte"] = (
    df["mortos"] > 0
).astype("int8")

# 5. Criar indicador de inconsistência
df["soma_categorias"] = (
    df["mortos"]
    + df["feridos"]
    + df["ilesos"]
    + df["ignorados"]
)

df["inconsistente_pessoas"] = (
    df["pessoas"] != df["soma_categorias"]
)

# 6. Conferência final
print("\nBASE PREPARADA")
print("Dimensões:", df.shape)

print("\nTipos de dados:")
print(df.dtypes)

print("\nRegistros por ano:")
print(df["ano"].value_counts().sort_index())

print("\nInconsistências preservadas:")
print(df["inconsistente_pessoas"].sum())

# 7. Salvar em Parquet
arquivo_saida = (
    pasta_tratados / "acidentes_prf_2020_2025.parquet"
)

df.to_parquet(
    arquivo_saida,
    index=False
)

print("\nArquivo salvo com sucesso:")
print(arquivo_saida)

print("\nCOLUNAS DA BASE:")
print(df.columns.tolist())

print("\nAMOSTRA DOS DADOS:")
print(df[[
    "pessoas",
    "mortos",
    "feridos",
    "feridos_leves",
    "feridos_graves",
    "ilesos",
    "ignorados"
]].head(10).to_string(index=False))

print("\nVALORES AUSENTES:")
print(df.isna().sum().sort_values(ascending=False).head(15))
print("\n" + "=" * 50)
print("DIAGNÓSTICO COMPLEMENTAR")
print("=" * 50)

# 1. Conferir total de feridos
df["conferencia_feridos"] = (
    df["feridos"] !=
    (df["feridos_leves"] + df["feridos_graves"])
)

print("\nDivergências nos feridos:")
print(df["conferencia_feridos"].sum())

# 2. Inconsistências por ano
print("\nInconsistências por ano:")
print(
    df.groupby("ano")["inconsistente_pessoas"]
    .sum()
)

# 3. Percentual de inconsistências
print("\nPercentual de inconsistências:")
print(
    round(
        df["inconsistente_pessoas"].mean() * 100,
        2
    ),
    "%"
)

# 4. Verificar registros inconsistentes
print("\nExemplos de inconsistências:")

print(
    df.loc[
        df["inconsistente_pessoas"],
        [
            "ano",
            "pessoas",
            "mortos",
            "feridos",
            "feridos_leves",
            "feridos_graves",
            "ilesos",
            "ignorados"
        ]
    ].head(10).to_string(index=False)
)