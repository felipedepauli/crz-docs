import pandas as pd
import numpy as np
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

# Definindo a arquitetura do modelo
model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(2,))) # 2 features
model.add(Dense(128, activation='relu'))
model.add(Dense(128, activation='relu'))    # 3 hidden layers
model.add(Dense(4, activation='softmax'))   # 4 competitors

# Carregando os pesos
model.load_weights('darts_best.hdf5')

darts = pd.read_csv('./darts.csv')
coordinates = darts.drop(['competitor'], axis=1)
galerim = [ "Manuela", "Xico Galo", "Zita", "Zé Cachaça" ]


preds = model.predict(coordinates)

preds = np.array([galerim[np.argmax(pred)] for pred in preds])

print(preds)
