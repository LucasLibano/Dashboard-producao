Dashboard de Produção – Power BI

- Sobre o projeto

Neste projeto, desenvolvi um dashboard de produção no Power BI com o objetivo de simular um cenário real de análise de dados em ambiente industrial.

Trabalhei desde a preparação dos dados até a construção dos indicadores e visualizações, focando em gerar insights relevantes.

- Processo de desenvolvimento

Preparação dos dados:

Utilizei uma base de dados em Excel fornecida por um curso e realizei algumas etapas iniciais:

Criei um script em Python (Pandas) para converter o arquivo de Excel para CSV
Organizei a estrutura de pastas do projeto
Adicionei elementos visuais, como plano de fundo do dashboard

- Definição dos KPIs

Antes de iniciar a construção no Power BI, defini os principais indicadores que seriam analisados:

Total de horas trabalhadas,
Produtividade,
Eficiência,
Total de itens produzidos,
Peças aprovadas e rejeitadas,

- Tratamento de dados (Power BI)

No Power BI, utilizei Power Query para tratamento inicial e DAX para criação das métricas.

- Medidas criadas:

Horas Trabalhadas = SUM('BaseProdução'[Total Horas])

Total Aprovado = SUM('BaseProdução'[Qtd Aprovada])

Total Rejeitado = SUM('BaseProdução'[Qtd Rejeitada])

Total Produzido = [Total Aprovado] + [Total Rejeitado]

- Análise de produtividade

Para diferenciar horas produtivas e não produtivas, utilizei a coluna de ocorrências:

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

- Indicadores finais
Produtividade = [Horas Produtivas] / [Horas Trabalhadas]

Qualidade = [Total Aprovado] / [Total Produzido]

- Resultado

O dashboard final apresenta:

KPIs principais (Total Aprovado, Rejeitado, Horas Produtivas e Paradas)
Produção mensal
Indicadores de produtividade e qualidade
Filtros por operador e período

- Aprendizados

Durante o desenvolvimento, reforcei conceitos:

Uso de CALCULATE para análises condicionais
Diferença entre BLANK() e valores preenchidos
Operador <> como “diferente” em DAX
Importância de definir KPIs antes da construção do dashboard
