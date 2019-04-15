# coding: utf-8

import csv
import pandas as pd
import numpy as np

def abre_csv_e_cruza(caminho_dados_de_escolas, caminho_dados_finais_cruzados):
	tcu = pd.read_csv(caminho_dados_de_escolas) ## Lê os dados de infraestrutura

	nomes_escolas = list(set(avaliacao["CO_ESCOLA"]))
	dic = dict((k, []) for k in avaliacao.columns) ## INICIA NOVO DF COM COLUNAS DO DF ORIGINAL
	avaliacao_df = pd.DataFrame(dic)
	avaliacao_df.columns = avaliacao.columns ## REORGANIZA AS COLUNAS

	for esc in nomes_escolas:
		df_escola = avaliacao[avaliacao["CO_ESCOLA"] == esc] ## PEGA O DATAFRAME FILTRADO PELA ESCOLA
		ano_recente = df_escola["NU_ANO"].argmax() ## ENCONTRA O INDICE NO DATAFRAME FILTRADO DO MAIOR ANO
		linha = df_escola.loc[[ano_recente]] ## PEGA A LINHA DO INDICE
		avaliacao_df = avaliacao_df.append(linha) ## ADICIONA ESSA LINHA NO NOVO DATAFRAME

	avaliacao_geo = pd.merge(tcu, avaliacao_df, on='CO_ESCOLA', how='outer') ## Faz o cruzamento
	avaliacao_geo = avaliacao_geo[np.isfinite(avaliacao_geo["NU_ANO"])] ## Tira dados que não estão disponíveis
	
	avaliacao_geo.to_csv(caminho_dados_finais_cruzados, sep=',', index = False) ## Cria novo csv



# Pastas
pasta_dados = "../dados/"
pasta_dados_cruzados = "../dados_cruzados/"
considerando_privadas = pasta_dados_cruzados + "com_escolas_privadas/"
desconsiderando_privadas = pasta_dados_cruzados + "sem_escolas_privadas/"

# Caminho dos dados de infraestrutura
caminho_dados_de_escolas = pasta_dados + "TS_ESCOLA_2015.csv"
caminho_dados_de_escolas_n_privadas = pasta_dados + "TS_ESCOLA_2015_sem_escolas_privadas.csv"


## Abrir csv do ENEM
avaliacao = pd.read_csv(pasta_dados + "enem.csv")
df_medias = avaliacao[["NU_MEDIA_CN","NU_MEDIA_CH","NU_MEDIA_LP","NU_MEDIA_MT","NU_MEDIA_RED"]]
df_media_total = df_medias.mean(axis = 1)
avaliacao["NU_MEDIA_TOTAL"] = df_media_total

## Cruzamento entre avaliação e dados de infraestrutura para escolas de ensino médio desconsiderando escolas privadas
caminho_dados_finais_cruzados = desconsiderando_privadas + "enem.csv"
abre_csv_e_cruza(caminho_dados_de_escolas_n_privadas, caminho_dados_finais_cruzados)

## Cruzamento entre avaliação e dados de infraestrutura para escolas de ensino médio considerando escolas privadas
caminho_dados_finais_cruzados = considerando_privadas + "enem.csv"
abre_csv_e_cruza(caminho_dados_de_escolas, caminho_dados_finais_cruzados)



## Abrir csv dos anos finais do IDEB
avaliacao = pd.read_csv(pasta_dados + "ideb_anos_finais.csv")

## Cruzamento entre avaliação e dados de infraestrutura para escolas dos anos finais do IDEB desconsiderando escolas privadas
caminho_dados_finais_cruzados = desconsiderando_privadas + "ideb_anos_finais.csv"
abre_csv_e_cruza(caminho_dados_de_escolas_n_privadas, caminho_dados_finais_cruzados)

## Cruzamento entre avaliação e dados de infraestrutura para escolas dos anos finais do IDEB considerando escolas privadas
caminho_dados_finais_cruzados = considerando_privadas + "ideb_anos_finais.csv"
abre_csv_e_cruza(caminho_dados_de_escolas, caminho_dados_finais_cruzados)



## Abrir csv dos anos finais do IDEB
avaliacao = pd.read_csv(pasta_dados + "ideb_anos_iniciais.csv")

## Cruzamento entre avaliação e dados de infraestrutura para escolas dos anos inciais do IDEB privadas e públicas
caminho_dados_finais_cruzados = desconsiderando_privadas + "ideb_anos_iniciais.csv"
abre_csv_e_cruza(caminho_dados_de_escolas_n_privadas, caminho_dados_finais_cruzados)

## Cruzamento entre avaliação e dados de infraestrutura para escolas dos anos inciais do IDEB considerando escolas privadas
caminho_dados_finais_cruzados = considerando_privadas + "ideb_anos_iniciais.csv"
abre_csv_e_cruza(caminho_dados_de_escolas, caminho_dados_finais_cruzados)


## Só creches
creches = pd.read_csv(caminho_dados_de_escolas)
creches = creches[creches["NO_ESCOLA"].str.contains('CRECHE', regex=False)]

creches.to_csv(considerando_privadas + "creches.csv", sep=',', index = False)
creches.to_csv(desconsiderando_privadas + "creches.csv", sep=',', index = False)
