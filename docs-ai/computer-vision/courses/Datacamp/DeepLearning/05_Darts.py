import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# Read in darts contestant data
darts = pd.read_csv('./darts.csv')

# Print general information about the DataFrame
print(darts.info())
print(darts.describe())

print("----------------------------------------")

# Print the original 'competitor' column
print("Original competitors:")
print(darts.competitor)
print(darts.head())

# Convert the 'competitor' column into a categorical data type
# This helps Pandas understand that the values are distinct categories
darts.competitor = pd.Categorical(darts.competitor)
print("After converting to categorical:")
print(darts.head())
print(darts.competitor)  # At the end of the column, it shows the categories

# Label encoding: Convert categories to numerical codes (0, 1, 2, ...)
# This step transforms the categories into a numerical representation
print("Label encoding (numerical codes for each category):")
print(darts.competitor.cat.codes)

print("----------------------------------------")

# Drop the 'competitor' column to get only the coordinates
coordinates = darts.drop(['competitor'], axis=1)
print("Coordinates (features):")
print(coordinates)

# One-Hot Encoding: Convert numerical codes to one-hot vectors
# Each category is represented by a binary vector where one element is "hot" (1) and others are "cold" (0)
competitors = to_categorical(darts.competitor.cat.codes)
print('One-hot encoded competitors (target labels):')
print(competitors)

model = Sequential()

print(coordinates.shape)

model.add(Dense(128, activation='relu', input_shape=(2,))) # 2 features
model.add(Dense(128, activation='relu'))
model.add(Dense(128, activation='relu'))    # 3 hidden layers
model.add(Dense(4, activation='softmax'))   # 4 competitors

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

stop_training = EarlyStopping(monitor='val_loss', patience=10)
save_best = ModelCheckpoint('darts_best.hdf5', save_best_only=True)

history = model.fit(
    coordinates,
    competitors,
    epochs=1000000,
    validation_data=(coordinates, competitors),
    callbacks=[stop_training, save_best]
)

accuracy = model.evaluate(coordinates, competitors)[1]

print('Accuracy:', accuracy)

plt.figure()
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Test'], loc='upper left')

plt.show()

preds = model.predict(coordinates)

galerim = [ "Manuela", "Xico Galo", "Zita", "Zé Cachaça" ]

preds = np.array([galerim[np.argmax(pred)] for pred in preds])

print(np.unique(preds, return_counts=True))
