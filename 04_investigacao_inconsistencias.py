
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

    df["arquivo_origem"] = arquivo.name
    lista_dados.append(df)

df = pd.concat(lista_dados, ignore_index=True)

# Calcular a soma das categorias de pessoas
df["soma_categorias"] = (
    df["mortos"]
    + df["feridos"]
    + df["ilesos"]
    + df["ignorados"]
)

# Calcular a diferença
df["diferenca_pessoas"] = (
    df["pessoas"] - df["soma_categorias"]
)

# Filtrar inconsistências
inconsistentes = df[
    df["diferenca_pessoas"] != 0
].copy()

# Extrair o ano
inconsistentes["ano"] = pd.to_datetime(
    inconsistentes["data_inversa"]
).dt.year

print("=" * 60)
print("INVESTIGAÇÃO DAS INCONSISTÊNCIAS")
print("=" * 60)

# 1. Quantidade por ano
print("\n1. INCONSISTÊNCIAS POR ANO")

print(
    inconsistentes.groupby("ano")
    .size()
    .to_string()
)

# 2. Direção das diferenças
print("\n2. DISTRIBUIÇÃO DAS DIFERENÇAS")

print(
    inconsistentes["diferenca_pessoas"]
    .value_counts()
    .head(15)
    .to_string()
)

# 3. Estatísticas das diferenças
print("\n3. RESUMO DAS DIFERENÇAS")

print(
    inconsistentes["diferenca_pessoas"]
    .describe()
)

# 4. Exemplos de registros
print("\n4. EXEMPLOS DE INCONSISTÊNCIAS")

colunas = [
    "id",
    "data_inversa",
    "uf",
    "municipio",
    "pessoas",
    "mortos",
    "feridos",
    "ilesos",
    "ignorados",
    "soma_categorias",
    "diferenca_pessoas"
]

print(
    inconsistentes[colunas]
    .head(15)
    .to_string(index=False)
)

print("\nINVESTIGAÇÃO CONCLUÍDA!")
