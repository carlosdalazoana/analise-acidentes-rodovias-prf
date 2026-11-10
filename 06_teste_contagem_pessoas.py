
import pandas as pd
from pathlib import Path

arquivos = sorted(
    Path("Dados/Brutos").glob("datatran*.csv")
)

bases = []

for arquivo in arquivos:
    bases.append(
        pd.read_csv(
            arquivo,
            sep=";",
            encoding="latin1"
        )
    )

df = pd.concat(bases, ignore_index=True)

# Soma sem ignorados
df["soma_sem_ignorados"] = (
    df["mortos"]
    + df["feridos"]
    + df["ilesos"]
)

# Soma incluindo ignorados
df["soma_com_ignorados"] = (
    df["soma_sem_ignorados"]
    + df["ignorados"]
)

print("=" * 60)
print("TESTE DE CONTAGEM DE PESSOAS")
print("=" * 60)

# Comparação das duas regras
print("\n1. PESSOAS = MORTOS + FERIDOS + ILESOS")

print(
    (df["pessoas"] == df["soma_sem_ignorados"])
    .value_counts()
)

print("\n2. PESSOAS = MORTOS + FERIDOS + ILESOS + IGNORADOS")

print(
    (df["pessoas"] == df["soma_com_ignorados"])
    .value_counts()
)

# Casos em que a soma sem ignorados coincide
print("\n3. REGISTROS EM QUE A SOMA SEM IGNORADOS COINCIDE")

coincidem = df[
    df["pessoas"] == df["soma_sem_ignorados"]
]

print("Quantidade:", len(coincidem))

# Exemplos
print("\n4. EXEMPLOS")

print(
    coincidem[
        [
            "id", "pessoas", "mortos",
            "feridos", "ilesos", "ignorados"
        ]
    ].head(10).to_string(index=False)
)

print("\nTESTE CONCLUÍDO!")
