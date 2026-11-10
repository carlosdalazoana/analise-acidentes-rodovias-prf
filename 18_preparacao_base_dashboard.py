import pandas as pd
from pathlib import Path

# Caminho principal do projeto
PASTA_PROJETO = Path(__file__).resolve().parent

# Caminho da base tratada
CAMINHO_BASE = PASTA_PROJETO / "Dados" / "Tratados" / "acidentes_prf_2020_2025.parquet"

# Leitura da base
df = pd.read_parquet(CAMINHO_BASE)

# Seleção do período oficial do projeto: 2021 a 2025
df = df[df["ano"].between(2021, 2025)].copy()

# Conferência inicial
print("BASE PARA O DASHBOARD")
print("-" * 40)
print(f"Total de registros: {len(df):,}")
print(f"Total de colunas: {len(df.columns)}")
print(f"Período: {df['ano'].min()} a {df['ano'].max()}")
print("\nColunas disponíveis:")
print(df.columns.tolist())
# Colunas selecionadas para o dashboard
colunas_dashboard = [
    "id",
    "data_inversa",
    "dia_semana",
    "horario",
    "uf",
    "br",
    "km",
    "municipio",
    "causa_acidente",
    "tipo_acidente",
    "classificacao_acidente",
    "fase_dia",
    "condicao_metereologica",
    "tipo_pista",
    "tracado_via",
    "pessoas",
    "mortos",
    "feridos_leves",
    "feridos_graves",
    "ilesos",
    "feridos",
    "veiculos",
    "ano",
    "mes",
    "possui_morte"
]

# Criar base reduzida
df_dashboard = df[colunas_dashboard].copy()

print("\nBASE REDUZIDA PARA O DASHBOARD")
print("-" * 40)
print(f"Registros: {len(df_dashboard):,}")
print(f"Colunas: {len(df_dashboard.columns)}")
print(df_dashboard.columns.tolist())
# Verificação de valores nulos
print("\nVERIFICAÇÃO DE VALORES NULOS")
print("-" * 40)

nulos = df_dashboard.isnull().sum()

print(nulos[nulos > 0])

print("\nTotal de células nulas:", nulos.sum())
# Exportação da base para CSV
PASTA_TRATADOS = PASTA_PROJETO / "Dados" / "Tratados"

CAMINHO_CSV = PASTA_TRATADOS / "acidentes_dashboard_2021_2025.csv"

df_dashboard.to_csv(
    CAMINHO_CSV,
    index=False,
    encoding="utf-8-sig",
    sep=","
)

print("\nEXPORTAÇÃO CONCLUÍDA")
print("-" * 40)
print(f"Arquivo salvo em: {CAMINHO_CSV}")
print(f"Registros exportados: {len(df_dashboard):,}")
print(f"Colunas exportadas: {len(df_dashboard.columns)}")
print(f"Tamanho do arquivo: {CAMINHO_CSV.stat().st_size / (1024 * 1024):.2f} MB")