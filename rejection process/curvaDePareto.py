import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
import graphviz
from IPython import embed
import pickle
import os


caminho = 'predictionsRejeitadas/'
caminho_list = (os.listdir(caminho))
saida = 'predictionsRejeitadasPareto/'


for data in caminho_list:

    lista = []
    lista_dominada = []

    arq_write = open(saida + data + 'CurvaPareto.csv', 'w')
    arq_write.write('limiarNorm;limiarAtk;TN;FP;FN;TP;REJ;TNR;TPR;AVG;REJ;ERRO;\n')

    with open(caminho + data) as f:
       for i, linha in enumerate(f):
           if i >= 1:
               lista.append(linha)
               lista_dominada.append(False)

    i = -1
    for linha1 in lista:
        i = i + 1
        if(lista_dominada[i] == True):
            continue
        j = -1
        for linha2 in lista:

            j = j + 1

            linha1split = linha1.split(";")
            linha2split = linha2.split(";")

            rej_1 = linha1split[10]
            erro_1 = linha1split[11]
            rej_2 = linha2split[10]
            erro_2 = linha2split[11]

            rej_1 = float(rej_1)
            rej_2 = float(rej_2)
            erro_1 = float(erro_1)
            erro_2 = float(erro_2)

            if(rej_1 < rej_2 and erro_1 < erro_2):
               lista_dominada[j] = True

    for i in range(len(lista_dominada)):
        if(lista_dominada[i] == False):
            arq_write.write(lista[i])
    arq_write.close()