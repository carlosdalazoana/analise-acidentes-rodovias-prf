
import pandas as pd
from pathlib import Path

# Caminho da pasta com os dados originais
pasta_dados = Path("Dados/Brutos")

# Localizar os arquivos CSV
arquivos = sorted(pasta_dados.glob("datatran*.csv"))

print("=" * 60)
print("INSPEÇÃO INICIAL - ACIDENTES PRF")
print("=" * 60)

for arquivo in arquivos:

    print(f"\nArquivo: {arquivo.name}")

    # Leitura inicial de cinco registros
    df = pd.read_csv(
        arquivo,
        sep=";",
        encoding="latin1",
        nrows=5
    )

    print("\nColunas encontradas:")
    print(df.columns.tolist())

    print("\nPrimeiros registros:")
    print(df.head())

    print("\nDimensões da amostra:")
    print(df.shape)

    print("-" * 60)

import pandas as pd
from pathlib import Path

pasta_dados = Path("Dados/Brutos")

arquivos = sorted(pasta_dados.glob("datatran*.csv"))

print("=" * 60)
print("DIMENSIONAMENTO DA BASE DE ACIDENTES - PRF")
print("=" * 60)

total_registros = 0

for arquivo in arquivos:

    df = pd.read_csv(
        arquivo,
        sep=";",
        encoding="latin1"
    )

    quantidade_linhas = len(df)
    quantidade_colunas = len(df.columns)

    total_registros += quantidade_linhas

    print(f"\nArquivo: {arquivo.name}")
    print(f"Registros: {quantidade_linhas:,}")
    print(f"Colunas: {quantidade_colunas}")

    print(
        f"Período: {df['data_inversa'].min()} "
        f"até {df['data_inversa'].max()}"
    )

    print("-" * 60)

print("\nTOTAL GERAL DE REGISTROS:")
print(f"{total_registros:,}")

print("=" * 60)


import pandas as pd
from pathlib import Path

pasta_dados = Path("Dados/Brutos")

arquivos = sorted(pasta_dados.glob("datatran*.csv"))

lista_dados = []

# Carregar e reunir os arquivos
for arquivo in arquivos:

    df = pd.read_csv(
        arquivo,
        sep=";",
        encoding="latin1"
    )

    lista_dados.append(df)

# Unificar as bases
df_acidentes = pd.concat(lista_dados, ignore_index=True)

print("=" * 60)
print("AUDITORIA DA QUALIDADE DOS DADOS - PRF")
print("=" * 60)

# 1. Dimensão da base
print("\n1. DIMENSÕES DA BASE")
print(df_acidentes.shape)

# 2. Valores ausentes
print("\n2. VALORES AUSENTES POR COLUNA")

nulos = df_acidentes.isnull().sum()

percentual_nulos = (
    df_acidentes.isnull().mean() * 100
).round(2)

relatorio_nulos = pd.DataFrame({
    "Quantidade_Nulos": nulos,
    "Percentual_Nulos": percentual_nulos
})

print(
    relatorio_nulos.sort_values(
        by="Quantidade_Nulos",
        ascending=False
    )
)

# 3. Duplicidades
print("\n3. REGISTROS DUPLICADOS")

print(
    "Linhas duplicadas:",
    df_acidentes.duplicated().sum()
)

print(
    "IDs duplicados:",
    df_acidentes["id"].duplicated().sum()
)

# 4. Tipos de dados
print("\n4. TIPOS DE DADOS")

print(df_acidentes.dtypes)

# 5. Resumo estatístico
print("\n5. RESUMO ESTATÍSTICO")

print(
    df_acidentes[
        ["pessoas", "mortos", "feridos_leves",
         "feridos_graves", "ilesos", "veiculos"]
    ].describe()
)

print("\nAUDITORIA FINALIZADA!")
