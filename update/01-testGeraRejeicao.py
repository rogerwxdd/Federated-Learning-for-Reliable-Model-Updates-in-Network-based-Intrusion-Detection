from IPython import embed

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Activation, Dense
from numpy import average
from numpy import array
from keras.models import clone_model
from tensorflow.keras.utils import to_categorical
from tensorflow import keras
from sklearn.metrics import confusion_matrix


dataView = 'ORUNADA'

caminho_dataset = 'dataset/'
dataset = ['ORUNADA2014_B12.csv']
modelUse = '11'

for data in dataset:
  df = pd.read_csv(caminho_dataset + data)
  df = df.sample(frac=1).reset_index(drop=True)
  x = df.drop('class', axis=1)
  inputs = np.asarray(x)
  inputs = MinMaxScaler().fit_transform(inputs)
  labels = np.asarray(df['class'])
  labels = to_categorical(labels)

  modelFederado = keras.models.load_model('saveModel/ORUNADA2014_B' + modelUse)

  pred = modelFederado.predict(inputs).argmax(axis=1)
  y_test = labels.argmax(axis=1)
  print("\nDataset: " + data)

  cm_dt = confusion_matrix(pred, y_test)
  TN = cm_dt[0][0]
  FN = cm_dt[0][1]
  FP = cm_dt[1][0]
  TP = cm_dt[1][1]
  AccTN = TN / (TN + FP)
  AccTP = TP / (TP + FN)

  print('TN: ' + str(TN) + ' | FP: ' + str(FP) + ' | FN: ' + str(FN) + ' | TP: ' + str(TP))
  print('AccTN: ' + str(AccTN) + ' | AccTP: ' + str(AccTP))

  pred_prob = modelFederado.predict(inputs)

  p_prob = []
  for i in pred_prob:
    p_prob.append(i)

  x = x.values.tolist()

  dt_write = open('predictions/rej'+data, 'w')
  dt_write.write('arquivo,classe,predicao,prob_norm,prob_atk,\n')

  for i in range(len(p_prob)):

    atk = p_prob[i][0]
    atk = '{:f}'.format(atk)
    norm = p_prob[i][1]
    norm = '{:f}'.format(norm)

    dt_write.write('arq,' + str(y_test[i])  + ','+ str(pred[i]) + ',' + atk + ',' + norm + ',\n')

  dt_write.close()

