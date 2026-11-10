
import pandas as pd
from pathlib import Path

pasta_dados = Path("Dados/Brutos")

arquivos = sorted(pasta_dados.glob("datatran*.csv"))

lista_dados = []

for arquivo in arquivos:
    df = pd.read_csv(
        arquivo,
        sep=";",
        encoding="latin1"
    )

    lista_dados.append(df)

df_acidentes = pd.concat(lista_dados, ignore_index=True)

print("=" * 60)
print("ANÁLISE DE CONSISTÊNCIA DOS DADOS")
print("=" * 60)

# REGRA 1: Conferir quantidade de pessoas
df_acidentes["soma_pessoas"] = (
    df_acidentes["mortos"]
    + df_acidentes["feridos"]
    + df_acidentes["ilesos"]
    + df_acidentes["ignorados"]
)

inconsistencia_pessoas = df_acidentes[
    df_acidentes["pessoas"] != df_acidentes["soma_pessoas"]
]

print("\n1. CONSISTÊNCIA DA QUANTIDADE DE PESSOAS")

print("Total de registros:", len(df_acidentes))
print("Inconsistências:", len(inconsistencia_pessoas))

# REGRA 2: Conferir quantidade de feridos
df_acidentes["soma_feridos"] = (
    df_acidentes["feridos_leves"]
    + df_acidentes["feridos_graves"]
)

inconsistencia_feridos = df_acidentes[
    df_acidentes["feridos"] != df_acidentes["soma_feridos"]
]

print("\n2. CONSISTÊNCIA DA QUANTIDADE DE FERIDOS")

print("Inconsistências:", len(inconsistencia_feridos))

# REGRA 3: Investigar valores extremos
print("\n3. MAIORES OCORRÊNCIAS COM MORTES")

colunas = [
    "id",
    "data_inversa",
    "uf",
    "municipio",
    "pessoas",
    "mortos",
    "feridos",
    "veiculos"
]

print(
    df_acidentes.nlargest(10, "mortos")[colunas]
    .to_string(index=False)
)

# REGRA 4: Investigar campos de texto vazios
print("\n4. CAMPOS DE TEXTO VAZIOS")

colunas_texto = df_acidentes.select_dtypes(
    include=["object", "str"]
).columns

for coluna in colunas_texto:

    vazios = (
        df_acidentes[coluna]
        .fillna("")
        .astype(str)
        .str.strip()
        .eq("")
        .sum()
    )

    if vazios > 0:
        print(f"{coluna}: {vazios} valores vazios")

print("\nANÁLISE CONCLUÍDA!")
