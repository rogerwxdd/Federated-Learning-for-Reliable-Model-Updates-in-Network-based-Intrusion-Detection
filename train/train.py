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
import sklearn
import tensorflow as tf
from tensorflow.keras.optimizers import Adam

EPOCHS = 5
NWORKERS = 5
EPOCHS_WORKER = 50
CLIENT_LR = 0.01
SERVER_LR = 0.1

def fedAvg(members):
    n_layers = len(members[0].get_weights())
    weights = [1.0 / len(members) for _ in range(len(members))]
    avg_model_weights = list()
    for layer in range(n_layers):
        layer_weights = array([model.get_weights()[layer] for model in members])
        avg_layer_weights = average(layer_weights, axis=0, weights=weights)
        avg_model_weights.append(avg_layer_weights)
    model = clone_model(members[0])
    model.set_weights(avg_model_weights)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def geraNModelosCopiaFederado(modeloFederado, n):
    modelos = [clone_model(modeloFederado) for _ in range(n)]
    for modelo in modelos:
        modelo.set_weights(modeloFederado.get_weights())
        modelo.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return modelos

numDataView = 21
data = 'data.csv'

df = pd.read_csv(data)
df = df.sample(frac=1).reset_index(drop=True)
x = df.drop('class', axis=1)
inputs = np.asarray(x)

inputs = MinMaxScaler().fit_transform(inputs)
labels = np.asarray(df['class'])
labels = to_categorical(labels)
lista_dataset_x = []
lista_dataset_y = []

# Divisão dos dados para os N workers
for i in range(NWORKERS):
    inicio = i * int(len(inputs) / NWORKERS)
    fim = (i + 1) * int(len(inputs) / NWORKERS)
    x = inputs[inicio:fim]
    y = labels[inicio:fim]
    lista_dataset_x.append(x)
    lista_dataset_y.append(y)

def create_server_model():
    modelFederado = Sequential()
    modelFederado.add(Dense(500, activation='relu', input_dim=numDataView))
    modelFederado.add(Dense(100, activation='relu'))
    modelFederado.add(Dense(50, activation='relu'))
    modelFederado.add(Dense(2, activation='softmax'))
    return modelFederado

def create_client_model(server_model):
    model = clone_model(server_model)
    model.set_weights(server_model.get_weights())
    optimizer = Adam(learning_rate=CLIENT_LR)
    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def client_update(model, dataset_x, dataset_y, epochs):
    model.fit(dataset_x, dataset_y, epochs=epochs, verbose=0)
    return model

def server_aggregate(client_models):
    server_weights = [model.get_weights() for model in client_models]
    aggregated_weights = np.mean(server_weights, axis=0)
    return aggregated_weights

server_model = create_server_model()
client_models = geraNModelosCopiaFederado(server_model, NWORKERS)

for i in range(1, EPOCHS + 1):
    print('Epoch [{:2d}/{:2d}]'.format(i, EPOCHS))
    client_updates = []
    for j in range(len(client_models)):
        client_model = create_client_model(server_model)
        client_model = client_update(client_model, lista_dataset_x[j], lista_dataset_y[j], EPOCHS_WORKER)
        client_updates.append(client_model)
        _, accuracy = client_model.evaluate(lista_dataset_x[j], lista_dataset_y[j], verbose=0)
        print('\tAccuracy: [{:2d}/{:2d}] na época [{:2d}]: {:.2f}%'.format(j, len(client_models), i, accuracy*100))

    aggregated_weights = server_aggregate(client_updates)
    server_model.set_weights(aggregated_weights)
    server_optimizer = Adam(learning_rate=SERVER_LR)
    server_model.compile(optimizer=server_optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

    for j in range(len(client_models)):
        client_models[j].set_weights(server_model.get_weights())

server_model.save('saveModel/txt' + str(data))