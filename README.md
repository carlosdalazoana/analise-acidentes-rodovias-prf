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
Os arquivos foram obtidos em formato CSV no portal de dados abertos da PRF. A coleta contemplou os arquivos DATATRAN de 2020 a 2025, que foram posteriormente carregados e consolidados utilizando Python e Pandas.


## Modelagem dos dados

Os arquivos DATATRAN da Polícia Rodoviária Federal, referentes ao período de 2020 a 2025, foram consolidados em uma única base utilizando Python e Pandas.

Durante a preparação dos dados, foram realizadas as seguintes operações:

- Padronização e conversão dos tipos de dados.
- Conversão da coluna de data e extração de ano, mês e dia.
- Tratamento de variáveis numéricas e geográficas.
- Criação de indicadores para identificar acidentes com mortes.
- Verificação de registros duplicados, valores ausentes e inconsistências.
- Preservação dos registros inconsistentes, sem alterações arbitrárias.

A base consolidada foi armazenada no formato Parquet, mantendo os dados preparados para as análises exploratórias.

Para a construção do dashboard, foi gerada uma base específica em CSV, considerando o período de 2021 a 2025. Essa delimitação foi adotada para garantir maior comparabilidade nas análises de causas dos acidentes, devido à mudança na classificação entre 2020 e 2021.

Os dados preparados foram utilizados na elaboração das análises exploratórias em Python e posteriormente disponibilizados no Looker Studio para construção das visualizações interativas.

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

A análise dos dados da Polícia Rodoviária Federal (PRF), considerando o período de 2021 a 2025, permitiu identificar padrões importantes relacionados à ocorrência e à gravidade dos acidentes nas rodovias federais brasileiras.

### 1. Evolução dos acidentes e mortes

- Em 2021, foram registrados 64.567 acidentes e 5.397 mortes.
- Em 2024, ocorreu o maior volume da série analisada, com 73.202 acidentes e 6.163 mortes.
- Em 2025, foram registrados 72.529 acidentes e 6.043 mortes.
- Na comparação entre 2021 e 2025, houve aumento aproximado de 12,3% nos acidentes e de 12% nas mortes.

### 2. Distribuição geográfica

A distribuição dos acidentes e das mortes apresenta diferenças importantes entre as unidades federativas. Os resultados permitem identificar estados com maior concentração de registros e outros que merecem atenção pela gravidade dos acidentes.

### 3. Causas associadas aos acidentes fatais

Entre as causas com maior número de mortes no período, destacam-se:

- Transitar na contramão: 4.163 mortes.
- Ausência de reação do condutor: 3.257 mortes.
- Reação tardia ou ineficiente do condutor: 2.845 mortes.
- Velocidade incompatível: 2.568 mortes.
- Ultrapassagem indevida: 1.891 mortes.

Esses resultados evidenciam a importância de ações preventivas relacionadas ao comportamento dos condutores e à segurança viária.

### 4. Gravidade dos acidentes

A análise da letalidade identificou causas que, embora apresentem menor volume de registros, possuem elevada proporção de acidentes com mortes. Entre elas, destacam-se o suicídio (presumido), acidentes envolvendo pedestres na pista e entrada inopinada de pedestres na via.

### 5. Distribuição temporal

- Dezembro apresentou o maior número de acidentes e mortes entre os meses analisados.
- Sábados e domingos concentraram os maiores volumes de acidentes.
- O horário das 18h apresentou o maior número de acidentes.
- O horário das 19h registrou o maior número de mortes.

### Considerações gerais

Os resultados mostram que os acidentes rodoviários apresentam padrões temporais, geográficos e comportamentais que podem contribuir para o planejamento de ações preventivas.

As análises devem ser interpretadas considerando as limitações dos registros administrativos da PRF e a ausência de dados de exposição ao trânsito, como volume de veículos e distância percorrida. Portanto, os números absolutos não representam, isoladamente, o risco individual de sofrer um acidente.

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

