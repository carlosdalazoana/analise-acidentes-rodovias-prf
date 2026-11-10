
import pandas as pd
from pathlib import Path

pasta = Path(__file__).parent
arquivo = pasta / "Dados" / "Tratados" / "acidentes_prf_2020_2025.parquet"

df = pd.read_parquet(arquivo)

print("=" * 60)
print("VERIFICAÇÃO DAS CAUSAS EM 2020")
print("=" * 60)

for ano in [2020, 2021]:
    print(f"\nANO: {ano}")

    dados = df[df["ano"] == ano]

    print("\nTOP 15 CAUSAS:")

    print(
        dados["causa_acidente"]
        .value_counts()
        .head(15)
        .to_string()
    )

    print("\nTOTAL DE CAUSAS DIFERENTES:")
    print(dados["causa_acidente"].nunique())

print("\nINVESTIGAÇÃO CONCLUÍDA!")
