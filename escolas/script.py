# coding: utf-8

import csv
import pandas as pd
import numpy as np

def abre_csv_e_cruza(caminho_dados_de_escolas, caminho_dados_finais_cruzados):
	tcu = pd.read_csv(caminho_dados_de_escolas)

	nomes_escolas = list(set(avaliacao["CO_ESCOLA"]))
	dic = dict((k, []) for k in avaliacao.columns) ## INICIA NOVO DF COM COLUNAS DO DF ORIGINAL
	avaliacao_df = pd.DataFrame(dic)
	avaliacao_df.columns = avaliacao.columns ## REORGANIZA AS COLUNAS

	for esc in nomes_escolas:
		df_escola = avaliacao[avaliacao["CO_ESCOLA"] == esc] ## PEGA O DATAFRAME FILTRADO PELA ESCOLA
		ano_recente = df_escola["NU_ANO"].argmax() ## ENCONTRA O INDICE NO DATAFRAME FILTRADO DO MAIOR ANO
		linha = df_escola.loc[[ano_recente]] ## PEGA A LINHA DO INDICE
		avaliacao_df = avaliacao_df.append(linha) ## ADICIONA ESSA LINHA NO NOVO DATAFRAME

	avaliacao_geo = pd.merge(tcu, avaliacao_df, on='CO_ESCOLA', how='outer')
	avaliacao_geo = avaliacao_geo[np.isfinite(avaliacao_geo["NU_ANO"])]
	
	avaliacao_geo.to_csv(caminho_dados_finais_cruzados, sep=',', index = False)

## Abrir csv do ENEM

avaliacao = pd.read_csv("../dados/enem.csv")

df_medias = avaliacao[["NU_MEDIA_CN","NU_MEDIA_CH","NU_MEDIA_LP","NU_MEDIA_MT","NU_MEDIA_RED"]]
df_media_total = df_medias.mean(axis = 1)

avaliacao["NU_MEDIA_TOTAL"] = df_media_total

## Para sem escolas de ensino médio desconsiderando privadas e públicas

caminho_dados_de_escolas = "../dados/TS_ESCOLA_2015_sem_escolas_privadas.csv"
caminho_dados_finais_cruzados = "../dados_cruzados/sem_escolas_privadas/enem.csv"
abre_csv_e_cruza(caminho_dados_de_escolas, caminho_dados_finais_cruzados)

## Para com escolas de ensino médio privadas

caminho_dados_de_escolas = "../dados/TS_ESCOLA_2015.csv"
caminho_dados_finais_cruzados = "../dados_cruzados/com_escolas_privadas/enem.csv"
abre_csv_e_cruza(caminho_dados_de_escolas, caminho_dados_finais_cruzados)

## Abrir csv dos anos finais do IDEB

avaliacao = pd.read_csv("../dados/ideb_anos_finais.csv")

## Para sem escolas dos anos finais do IDEB privadas e públicas

caminho_dados_de_escolas = "../dados/TS_ESCOLA_2015_sem_escolas_privadas.csv"
caminho_dados_finais_cruzados = "../dados_cruzados/sem_escolas_privadas/ideb_anos_finais.csv"
abre_csv_e_cruza(caminho_dados_de_escolas, caminho_dados_finais_cruzados)

## Para sem escolas dos anos finais do IDEB privadas e desconsiderando públicas

caminho_dados_de_escolas = "../dados/TS_ESCOLA_2015.csv"
caminho_dados_finais_cruzados = "../dados_cruzados/com_escolas_privadas/ideb_anos_finais.csv"
abre_csv_e_cruza(caminho_dados_de_escolas, caminho_dados_finais_cruzados)

## Abrir csv dos anos finais do IDEB

avaliacao = pd.read_csv("../dados/ideb_anos_finais.csv")

## Para sem escolas dos anos finais do IDEB privadas e públicas

caminho_dados_de_escolas = "../dados/TS_ESCOLA_2015_sem_escolas_privadas.csv"
caminho_dados_finais_cruzados = "../dados_cruzados/sem_escolas_privadas/ideb_anos_inciais.csv"
abre_csv_e_cruza(caminho_dados_de_escolas, caminho_dados_finais_cruzados)

## Para sem escolas dos anos iniciais do IDEB privadas e desconsiderando públicas

caminho_dados_de_escolas = "../dados/TS_ESCOLA_2015.csv"
caminho_dados_finais_cruzados = "../dados_cruzados/com_escolas_privadas/ideb_anos_inciais.csv"
abre_csv_e_cruza(caminho_dados_de_escolas, caminho_dados_finais_cruzados)