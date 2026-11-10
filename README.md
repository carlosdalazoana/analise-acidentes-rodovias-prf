# Análise de Acidentes nas Rodovias Federais Brasileiras — PRF (2021–2025)

## Sobre o projeto

Projeto de análise exploratória de dados desenvolvido como parte do Projeto de Parceria da EBAC com a Semantix, com o objetivo de investigar o comportamento dos acidentes registrados nas rodovias federais brasileiras.

A partir dos dados públicos disponibilizados pela Polícia Rodoviária Federal (PRF), foram analisados padrões temporais, distribuição geográfica, causas dos acidentes e indicadores de gravidade.

O projeto busca transformar dados públicos em informações que contribuam para a compreensão dos acidentes rodoviários e apoiem discussões sobre segurança viária.

## Problema investigado

Os acidentes nas rodovias federais representam um importante desafio para a segurança pública. Entretanto, a análise isolada dos registros dificulta a identificação de padrões que podem ajudar a compreender quando, onde e em quais circunstâncias esses eventos acontecem.

Diante disso, este projeto procura responder às seguintes perguntas:

- Como evoluiu o número de acidentes e mortes ao longo dos anos?
- Quais estados concentram o maior número de acidentes?
- Quais estados apresentam maior proporção de acidentes fatais?
- Quais são as principais causas dos acidentes?
- Quais causas estão associadas a maior gravidade?
- Existem padrões relacionados ao mês, dia da semana e horário dos acidentes?
- Como a gravidade dos acidentes varia conforme o período do dia?

## Fonte de dados

Os dados foram obtidos no portal de dados abertos da Polícia Rodoviária Federal (PRF).

**Fonte:** [Dados Abertos da PRF](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos)

Foram utilizados os arquivos DATATRAN referentes aos anos de 2020 a 2025.

A base consolidada contém 406.255 registros e foi utilizada como ponto de partida para as etapas de preparação e análise.

Para garantir maior comparabilidade na análise das causas dos acidentes, as análises comparativas do dashboard consideram o período de 2021 a 2025, devido a diferenças na classificação das causas entre 2020 e 2021.

## Tecnologias utilizadas

- **Python:** preparação, tratamento e análise dos dados.
- **Pandas:** manipulação e transformação das bases.
- **Matplotlib:** criação de gráficos para análise exploratória.
- **PyArrow:** armazenamento dos dados tratados em formato Parquet.
- **Looker Studio:** construção do dashboard interativo.
- **Git e GitHub:** versionamento e documentação do projeto.

## Etapas do projeto

1. **Coleta de dados:** obtenção dos arquivos DATATRAN disponibilizados pela PRF.
2. **Inspeção inicial:** análise da estrutura, das colunas e dos tipos de dados.
3. **Tratamento e preparação:** conversão de tipos, criação de variáveis e consolidação dos arquivos.
4. **Auditoria da qualidade:** investigação de valores ausentes, duplicidades e inconsistências.
5. **Análise exploratória (EDA):** investigação de padrões temporais, geográficos, causas e gravidade.
6. **Visualização:** construção de gráficos e dashboard interativo no Looker Studio.
7. **Documentação:** registro da metodologia, dos resultados e das limitações encontradas.

## Principais análises realizadas

- Evolução anual dos acidentes e mortes.
- Distribuição dos acidentes por estado.
- Gravidade dos acidentes por estado.
- Principais causas dos acidentes.
- Evolução das causas ao longo dos anos.
- Evolução das causas associadas a acidentes fatais.
- Letalidade por causa do acidente.
- Distribuição dos acidentes por mês.
- Distribuição por dia da semana.
- Distribuição por horário e período do dia.

## Principais resultados e observações

As análises realizadas permitiram identificar padrões relevantes:

- Minas Gerais, Santa Catarina e Paraná aparecem entre os estados com maior volume de registros de acidentes no período analisado.
- Os registros apresentam concentração de acidentes nos finais de semana, especialmente aos domingos e sábados.
- Dezembro apresenta o maior volume de acidentes entre os meses analisados.
- O período noturno apresenta uma proporção maior de acidentes com mortes em relação ao total de acidentes registrados nesse período.
- Entre as causas com maior número de mortes estão transitar na contramão, ausência de reação do condutor e reação tardia ou ineficiente.

Os resultados representam padrões observados nos registros da PRF e não devem ser interpretados isoladamente como medidas de risco individual, pois não há dados de exposição ao tráfego, como volume de veículos ou distância percorrida.

## Qualidade e limitações dos dados

Durante a auditoria da base, foram identificados registros em que a quantidade total de pessoas envolvidas não corresponde à soma das categorias de vítimas e pessoas ilesas.

Essas inconsistências foram preservadas na base, sem exclusão ou correção arbitrária, para manter a rastreabilidade dos dados originais.

Também foi identificada uma mudança na classificação das causas dos acidentes entre 2020 e 2021. Por esse motivo, as análises comparativas de causas consideram o período de 2021 a 2025.

Os dados representam ocorrências registradas pela PRF e estão sujeitos às limitações de preenchimento e classificação dos registros administrativos.

## Dashboard interativo

[Visualizar dashboard — Análise de Acidentes nas Rodovias Federais (2021–2025)](https://datastudio.google.com/reporting/a060f52c-3058-444a-95de-81af737cbbff)

## Estrutura do repositório

```text
Projeto de Parceria-Semantix/
│
├── Dados/
│   └── Tratados/
│       └── Arquivos CSV das análises
│
├── 01_inspecao_inicial.py
├── 03_consistencia_dados.py
├── 04_investigacao_inconsistencias.py
├── ...
├── 18_preparacao_base_dashboard.py
│
├── eda_*.png
│
└── README.md
```

Os arquivos brutos e as bases completas foram mantidos localmente e não estão versionados no GitHub devido ao tamanho. Os scripts e arquivos de resultados menores permanecem disponíveis no repositório.

## Autor

Projeto desenvolvido por **Carlos Dalazoana** como parte da formação em Análise de Dados da EBAC.

[GitHub](https://github.com/carlosdalazoana)

