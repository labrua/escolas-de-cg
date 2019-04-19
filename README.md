# Escolas de Campina Grande

Dados e análises da distribuição e avaliação das escolas de Campina Grande - PB. 

Este repositório é uma tentativa de retratar a disponibilidade e qualidade da educação pública no ensino básico e médio em Campina Grande. Como os dados sobre disponibilidade e qualidade são criados com várias periodicidades, há algum desencontro na data de produção dos dados, e eles estão normalmente defasados. 

Neste repositório, usamos dados: 
    * sobre as escolas de 2015
    * sobre avaliação do ensino básico de 2017
    * sobre avaliação do ensino médio de 2015

A avaliação do ensino vem do Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP). Essa avaliação é baseada no desempenho dos alunos na prova do Exame Nacional do Ensino Médio (ENEM) e no Índice de Desenvolvimento da Educação Básica (IDEB). O IDEB por sua vez é calculado por indicadores de aprendizagem extraídos de dois exames:

1. o Sistema de Avaliação da Educação Básica (SAEB), composto pela Avaliação Nacional da Educação Básica (ANEB), Anresc/Prova Brasil e Avaliação Nacional da Alfabetização (ANA)
2. De indicadores do Censo Escolar, ou seja, relacionado índice de aprovação dos alunos ao longo dos anos letivos.


## Organização

`dados-brutos/` dados vindos das fontes primárias que usamos: 

  * `dados-brutos/TS_ESCOLA_2015.csv`: informações sobre infraestrutura e localização das escolas de CG, vindos de um repositório do TCU em comunicação privada.
  * `dados-brutos/ideb_anos_iniciais.csv` e `dados-brutos/ideb_anos_finais.csv` : avaliações das escolas no ensino fundamental, vindos do INEP. 
  * `dados-brutos/enem.csv`: desempenho das escolas que tem ensino médio no ENEM, vindos do INEP. 

`dados/` dados filtrados e cruzados sobre as escolas de CG.

`code/` código para importação e funções úteis às análises.

`reports/` análises em notebooks.


## Guia de uso

### Por que esses dados foram criados

Esses dados foram coletados como parte de uma pesquisa do LabRua que investiga a quantidade e a qualidade de equipamentos urbanos relacionados à saúde, educação e transporte em diferentes partes da cidade. A pesquisa está interessada em examinar se há correlação entre a falta de equipamentos públicos e a população carcerária oriunda de diferentes regiões da cidade.

### História, padrões e formato

Os dados deste repositório estão em csvs. Foram criados assim em 2018, a partir de fontes primárias em csv e xls.

### Contexto Organizacional

O LabRua é um laboratório de pesquisa sem fins lucrativos. Os dados foram criados por estudantes e professores do LabRua e Lab Analytics da UFCG. Os dados de fontes primárias vem do INEP, órgão do MEC e portanto do Governo Federal e também do Tribunal de Contas da União. Os dados do TCU foram criados por um grupo de trabalho do TCU interessado em acompanhar a gestão de educação no Brasil, e são essencialmente dados do próprio MEC enriquecidos pela geolocalização das escolas. Os dados do MEC são criados com o intuito de acompanhar a qualidade pública da educação pública e privada em todo o Brasil. 

### Fluxo de trabalho

Dados da existência, localização e infraestrutura das escolas vem do TCU provavelmente através do georreferenciamento dos dados das escolas publicados pelo MEC. 

Dados do INEP vem de: 

  * [Microdados do ENEM 2005-2015](http://download.inep.gov.br/microdados/enem_por_escola/2005_a_2015/microdados_enem_por_escola.zip) disponibilizados pelo ENEM e explicados por exemplo [neste link](http://ufcg.edu.br/prt_ufcg/assessoria_imprensa/mostra_noticia.php?codigo=21692). O zip no link possui um dicionário das variáveis.

  * [Microdados do IDEB de 2005 a 2017](http://portal.inep.gov.br/web/guest/educacao-basica/ideb/resultados) publicados no portal do INEP.

Esses dados foram filtrados para incluir apenas escolas de Campina Grande e cruzados com os dados do TCU com base nos nomes das escolas. 

Os resultados destes cruzamentos estão nas pastas `dados/`.

### O que você deve saber sobre os dados, incluindo limitações

A geolocalização realizada pelo TCU parece ter sido a partir do endereço da escola, e está sujeita a erros. Há escolas que existem hoje e não encontramos nos dados, e provavelmente há escolas que não estão nos dados e existem. Os detalhes da infraestrutura das escolas são autodeclarados pelas escolas. 

### Outros usos desses dados

Ainda não conhecemos. Se você usá-los, entra em contato para listarmos aqui. 

### Listagem de valores de campo, livro de códigos, etc.

As variáveis estão explicadas em 