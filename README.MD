#  Dashboard de Produção – Power BI

## Sobre o projeto

Dashboard de produção desenvolvido no Power BI para simular um cenário real de análise de dados em ambiente industrial. O projeto cobre todo o fluxo de trabalho: da preparação dos dados até a construção de indicadores e visualizações, com foco em gerar insights para tomada de decisão.

A base de dados simula a produção de peças de uma empresa industrial, com informações sobre horas trabalhadas, ocorrências e quantidade de itens aprovados e rejeitados.

---

## Tecnologias utilizadas

- **Power BI** – Construção do dashboard e visualizações
- **DAX** (Data Analysis Expressions) – Criação de medidas e indicadores
- **Power Query** – Tratamento e transformação dos dados
- **Python / Pandas** – Conversão do arquivo Excel para CSV
- **Excel** – Base de dados original

---

## Processo de desenvolvimento

### 1. Preparação dos dados

- Base de dados em Excel fornecida por um curso
- Criação de um script Python com **Pandas** para converter o arquivo `.xlsx` em `.csv`
- Organização da estrutura de pastas do projeto
- Criação de plano de fundo personalizado para o dashboard

### 2. Definição dos KPIs

Antes de iniciar a construção no Power BI, os indicadores foram planejados em um documento:

- Total de horas trabalhadas
- Horas produtivas e horas paradas
- Produtividade (%)
- Qualidade (%)
- Total de itens produzidos
- Peças aprovadas e peças rejeitadas

### 3. Tratamento de dados no Power BI

Os dados foram tratados com **Power Query** e as métricas criadas com **DAX**.

#### Medidas criadas:

```dax
Horas Trabalhadas = SUM('BaseProdução'[Total Horas])

Total Aprovado = SUM('BaseProdução'[Qtd Aprovada])

Total Rejeitado = SUM('BaseProdução'[Qtd Rejeitada])

Total Produzido = [Total Aprovado] + [Total Rejeitado]
```

#### Análise de horas produtivas vs. paradas:

A coluna de **Ocorrências** foi usada para diferenciar horas produtivas (sem ocorrência) de horas paradas (com ocorrência). A função `CALCULATE` foi utilizada por permitir cálculos com base em condições.

```dax
Horas Produtivas = 
CALCULATE(
    SUM('BaseProdução'[Total Horas]),
    'BaseProdução'[Ocorrência] = BLANK()
)

Horas Paradas = 
CALCULATE(
    SUM('BaseProdução'[Total Horas]),
    'BaseProdução'[Ocorrência] <> BLANK()
)
```

#### Indicadores de desempenho:

```dax
Produtividade = [Horas Produtivas] / [Horas Trabalhadas]

Qualidade = [Total Aprovado] / [Total Produzido]
```

---

## Resultado

O dashboard final apresenta:

- **KPIs principais** — Total Aprovado (3.084 Mil), Total Rejeitado (21 Mil), Horas Produtivas (30,96 Mil) e Horas Paradas (8,89 Mil)
- **Gráfico de barras** — Total aprovado por mês ao longo do ano
- **Indicadores de gauge** — Produtividade em **77,69%** e Qualidade em **99,32%**
- **Filtros interativos** — por Operador e por Mês, permitindo análise individual de cada funcionário

---

## Recursos visuais utilizados

- [mycolor.space](https://mycolor.space) – Paleta de cores do dashboard
- [Flaticon](https://www.flaticon.com) – Ícones dos cartões de KPI

---

## Aprendizados

- Uso do `CALCULATE` para cálculos condicionais no DAX
- Diferença entre `BLANK()` e valores preenchidos em colunas
- Operador `<>` como "diferente de" no DAX
- Importância de definir KPIs antes de começar a construir o dashboard
- Conversão de arquivos com Python/Pandas no início do pipeline de dados
