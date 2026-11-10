
import pandas as pd
from pathlib import Path

arquivos = sorted(
    Path("Dados/Brutos").glob("datatran*.csv")
)

df = pd.concat(
    [
        pd.read_csv(a, sep=";", encoding="latin1")
        for a in arquivos
    ],
    ignore_index=True
)

soma_sem_ignorados = (
    df["mortos"] + df["feridos"] + df["ilesos"]
)

soma_com_ignorados = (
    soma_sem_ignorados + df["ignorados"]
)

# Criar condições
df["ignorados_zero"] = df["ignorados"] == 0

df["coincide_sem_ignorados"] = (
    df["pessoas"] == soma_sem_ignorados
)

df["coincide_com_ignorados"] = (
    df["pessoas"] == soma_com_ignorados
)

print("=" * 60)
print("CRUZAMENTO DAS REGRAS DE CONTAGEM")
print("=" * 60)

print("\n1. COINCIDÊNCIA SEM IGNORADOS")

print(
    df.groupby("ignorados_zero")
    ["coincide_sem_ignorados"]
    .agg(["sum", "count"])
)

print("\n2. COINCIDÊNCIA COM IGNORADOS")

print(
    df.groupby("ignorados_zero")
    ["coincide_com_ignorados"]
    .agg(["sum", "count"])
)

print("\n3. REGISTROS COM IGNORADOS POSITIVOS")

print(
    df[df["ignorados"] > 0]
    [["pessoas", "mortos", "feridos",
      "ilesos", "ignorados"]]
    .head(10)
    .to_string(index=False)
)

print("\nCRUZAMENTO CONCLUÍDO!")
