# Escolas de Campina Grande

Este repositório é relacionado à dados das escolas e sua avaliação em Campina Grande, PB.

Finalidade: Esse repositório foi desenvolvido para uma proposta de pesquisa que visa investigar em diferentes regiões da cidade a quantidade e a qualidade de equipamentos urbanos relacionados à saúde, educação e transporte na esfera pública, para explorar se há correlação entre a oferta desses equipamentos e  população carcerária.

<B> 1. Finalidade original e aplicação: </B>

Os dados existem com a intenção de mostrar a qualidade em cada instituição pública de ensino.

<B> 2. História, padrões e formato: </B>

Os dados são foram disponibilizados em Comma-separated values (CSV).

<B> 3. Contexto Organizacional: </B>

Contextos organizacionais não afetam a natureza da qualidade dos dados.

<B> 4. Fluxo de trabalho: </B>

Inicialmente para tornar a pesquisa possível, foi necessário um levantamento de infraestrutura e de qualidade de serviços públicos educacionais. Diante dos dados, foi necessária uma etapa de refinamento dos mesmos. O objetivo é extrair dos dados brutos já coletados, informações específicas para a pesquisa. Com o produto final do refinamento, é feito um cruzamento, a fim de criar relações entre os mesmos.

A coleta de dados relacionados à localização e infraestrutura das escolas foi feita através das informações geradas pelo site do Tribunal de Contas da União (TCU). Já a coleta dos dados relacionados à qualidade do ensino foi feita através do Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP), que determina o desempenho das escolas de ensino médio e fundamental. Tal avaliação é baseada no desempenho dos alunos na prova do Exame Nacional do Ensino Médio (ENEM) e no Índice de Desenvolvimento da Educação Básica (IDEB)

O IDEB é calculado por indicadores de aprendizagem extraídos de dois exames:

01. o Sistema de Avaliação da Educação Básica (SAEB), composto pela Avaliação Nacional da Educação Básica (ANEB), Anresc/Prova Brasil e Avaliação Nacional da Alfabetização (ANA)

02. De indicadores do Censo Escolar, ou seja, relacionado índice de aprovação dos alunos ao longo dos anos letivos.

Após a análise, foi realizado um cruzamento de dados através de Pandas, que é uma biblioteca de Python, específica para manipulação e análise de dados. Essa ferramenta foi escolhida baseado na confiabilidade da manipulação dos dados e na familiaridade com a tecnologia do pesquisador.

<B> 5. O que você deve saber sobre os dados, incluindo limitações: </B>

Os dados tem algumas limitações por faltar dados de algumas escolas, como por exemplo: localização e pontos de sua infraestrutura.

<B> 6. Aplicações adicionais: </B>

Outras pessoas podem fazer uso desses dados com o objetivo de analisar a vitalidade urbana na cidade de Campina Grande.

<B> 7. Apêndice - listagem de valores de campo, livro de códigos, etc. </B>

Dados de infraestrutura das escolas: Dados obtidos através de requisições ao TCU

Avaliação do ENEM por escolas: http://ufcg.edu.br/prt_ufcg/assessoria_imprensa/mostra_noticia.php?codigo=21692

Avaliação do IDEB por escolas: http://portal.inep.gov.br/web/guest/educacao-basica/ideb/resultados

<B> 8. Fontes / Reconhecimentos </B>
