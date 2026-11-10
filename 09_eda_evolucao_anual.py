
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Carregar a base tratada
arquivo = Path(
    "Dados/Tratados/acidentes_prf_2020_2025.parquet"
)

df = pd.read_parquet(arquivo)

print("=" * 60)
print("EDA - EVOLUÇÃO ANUAL DOS ACIDENTES")
print("=" * 60)

# 2. Agrupar os dados por ano
analise_anual = df.groupby("ano").agg(
    acidentes=("id", "count"),
    mortes=("mortos", "sum"),
    acidentes_fatais=("possui_morte", "sum"),
    feridos=("feridos", "sum"),
    pessoas_envolvidas=("pessoas", "sum")
).reset_index()

# 3. Calcular variação percentual dos acidentes
analise_anual["variacao_acidentes_%"] = (
    analise_anual["acidentes"]
    .pct_change() * 100
).round(2)

# 4. Calcular variação percentual das mortes
analise_anual["variacao_mortes_%"] = (
    analise_anual["mortes"]
    .pct_change() * 100
).round(2)

# 5. Calcular percentual de acidentes fatais
analise_anual["percentual_acidentes_fatais"] = (
    analise_anual["acidentes_fatais"]
    / analise_anual["acidentes"] * 100
).round(2)

# 6. Exibir resultados
print("\nTABELA DE EVOLUÇÃO ANUAL")

print(
    analise_anual.to_string(index=False)
)

# 7. Criar gráfico de acidentes
plt.figure(figsize=(10, 5))

plt.plot(
    analise_anual["ano"],
    analise_anual["acidentes"],
    marker="o"
)

plt.title("Evolução anual dos acidentes - PRF")
plt.xlabel("Ano")
plt.ylabel("Quantidade de acidentes")
plt.xticks(analise_anual["ano"])
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(
    "eda_evolucao_acidentes.png",
    dpi=300
)

plt.show()

# 8. Criar gráfico de mortes
plt.figure(figsize=(10, 5))

plt.plot(
    analise_anual["ano"],
    analise_anual["mortes"],
    marker="o"
)

plt.title("Evolução anual das mortes - PRF")
plt.xlabel("Ano")
plt.ylabel("Quantidade de mortes")
plt.xticks(analise_anual["ano"])
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(
    "eda_evolucao_mortes.png",
    dpi=300
)

plt.show()

# 9. Salvar tabela para documentação
Path("Dados/Tratados").mkdir(
    parents=True,
    exist_ok=True
)

analise_anual.to_csv(
    "Dados/Tratados/evolucao_anual.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nANÁLISE CONCLUÍDA!")
print("Gráficos e tabela gerados com sucesso.")
