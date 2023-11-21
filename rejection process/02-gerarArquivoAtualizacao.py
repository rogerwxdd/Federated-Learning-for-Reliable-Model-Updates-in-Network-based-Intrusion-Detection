import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
import graphviz
from IPython import embed
import pickle
import os
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import precision_score, accuracy_score
import joblib
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier

saida = 'saida_predictions/'
caminho_pred = 'predictions/'
caminho_dataset = 'dataset/'
dataset = ['01']

for data in dataset:

    arq_write = open('resultado/resultado_' + data + '.csv', 'w')
    arq_write.write('Dataset;limiarNorm;limiarAtk;TN;FP;FN;TP;REJ;TNR;TPR;AVG;REJ_N;ERRO;\n')
    arq_csv = open('novo_dataset/ORUNADA_' + data + '.csv', 'w')

    novoDataset = []
    with open(caminho_dataset + 'Data_B' + str(data) + '.csv') as f:
        for i, linha in enumerate(f):
            if i >= 1:
                novoDataset.append(linha)

    arquivoPredictions = pd.read_csv(caminho_pred + 'rejData_B' + data + '.csv')
    lenArqPred = len(arquivoPredictions)

    predNorm = []
    predAtk = []
    predClasse = []
    for predNovo in range(lenArqPred):
        predNorm.append(float(arquivoPredictions['prob_norm'][predNovo]))
        predAtk.append(float(arquivoPredictions['prob_atk'][predNovo]))
        predClasse.append(int(arquivoPredictions['classe'][predNovo]))

    TN = 0
    FP = 0
    TP = 0
    FN = 0
    REJ = 0
    limiarAtk = 0.58
    limiarNorm = 0.73

    for pred in range(lenArqPred):
        if (predAtk[pred] >= predNorm[pred]):
            if (predAtk[pred] >= limiarAtk):
                if (predClasse[pred] == 1):
                    TP += 1
                else:
                    FP += 1
            else:
                REJ += 1
                arq_csv.write(novoDataset[pred])
        else:
            if (predNorm[pred] >= limiarNorm):
                if (predClasse[pred] == 0):
                    TN += 1
                else:
                    FN += 1
            else:
                REJ += 1
                arq_csv.write(novoDataset[pred])

    try:
        TNR = TN / (TN + FP)
    except:
        TNR = 0
    try:
        TPR = TP / (TP + FN)
    except:
        TPR = 0
    try:
        AVG = (TNR + TPR) / 2
    except:
        AVG = 0
    try:
        REJ_N = REJ / (TN + FP + FN + TP + REJ)
    except:
        REJ_N = 0
    try:
        ERRO = ((FP / (FP + TN)) + (FN / (FN + TP))) / 2
    except:
        ERRO = 0

    print('Lim_N:' + str(limiarNorm) + ' Lim_A:' + str(limiarAtk) + ' TN:' + str(TN) + ' FP:' + str(
        FP) + ' FN:' + str(FN) + ' TP:' + str(TP) + ' REJ:' + str(REJ))
    print('ERRO: ' + str(ERRO) + ' | TNR ' + str(TNR) + ' | TPR ' + str(TPR))

    arq_write.write(
        str(data) + ';' + str(limiarNorm) + ';' + str(limiarAtk) + ';' +
        str(TN) + ';' + str(FP) + ';' + str(FN) + ';' + str(TP) + ';' + str(REJ) + ';' +
        str(TNR) + ';' + str(TPR) + ';' + str(AVG) + ';' + str(REJ_N) + ';' + str(ERRO) + ';\n')

arq_write.close()