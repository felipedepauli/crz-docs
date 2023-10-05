import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
import cv2
import numpy as np
import random
import argparse
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist
from tensorflow.keras.callbacks import EarlyStopping


def train_model():
    # Load the MNIST dataset (MNIST = Modified National Institute of Standards and Technology database)
    # It's a dataset of 60,000 28x28 grayscale images of the 10 digits, along with a test set of 10,000 images.
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    # Transform the dataset to have values between 0 and 1 (normalization)
    X_train = X_train/255
    X_test  = X_test/255

    # One-hot encode the labels (transform the labels into a binary matrix)
    Y_train = to_categorical(y_train, num_classes=10)
    Y_test  = to_categorical(y_test, num_classes=10)

    # Reshape the dataset to fit the model (flatten the images)
    # We use -1 to infer the dimension of all the images in the dataset
    X_train = X_train.reshape((-1, 784))
    X_test  = X_test.reshape((-1, 784))

    # Instantiate a Sequential model
    model = Sequential()

    # Add Dense layers
    model.add(Dense(50, activation='relu', input_shape=(784,)))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(50, activation='relu'))

    # Add a final Dense layer with 10 neurons and softmax activation
    model.add(Dense(10, activation='softmax'))

    # Compile your model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Define an early stopping monitor
    # It will stop the training when the validation loss doesn't improve after 2 epochs
    early_stopping_monitor = EarlyStopping(patience=2)

    # Fit your model on the training data for 20 epochs (or less if the early stopping monitor is triggered)
    model.fit(X_train, Y_train, epochs=20, batch_size=10, validation_split=0.2, callbacks=[early_stopping_monitor])

    # Save the model
    model.save('mnist_model.h5')

def predict_model(image_path=None):
    # Load the saved model
    model = load_model('mnist_model.h5')

    if image_path is not None:
        # Load the image
        img = cv2.imread(image_path)
        cv2.imshow('Image', img)
        cv2.waitKey(0)

        # Make sure the image is grayscale
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Invert the colors if necessary
        img = cv2.bitwise_not(img)
        
        # Apply Gaussian blur
        img = cv2.GaussianBlur(img, (3, 3), 0)
        
        # Apply threshold
        _, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

        # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
     
        # Perform a morphological closing operation
        kernel = np.ones((3,3),np.uint8)
        img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

        
        # Perform a morphological closing operation
        kernel = np.ones((3,3),np.uint8)
        img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

        # Perform a morphological closing operation
        kernel = np.ones((7,7),np.uint8)
        img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)


        # Dilate the image to make the lines thicker
        kernel = np.ones((7,7),np.uint8)
        img = cv2.dilate(img, kernel, iterations = 1)

        
        # Perform a morphological opening operation
        kernel = np.ones((3,3),np.uint8)
        img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        
        # Perform a morphological closing operation
        kernel = np.ones((7,7),np.uint8)

        # Resize the image
        img = cv2.resize(img, (28, 28))

        # Normalize the image
        img = img / 255.0

        # Reshape the image for prediction
        img = img.reshape((1, 784))

        # Predict the digit
        prediction = model.predict(img)
        predicted_digit = np.argmax(prediction)

        # Write the predicted digit on the image
        img_disp = cv2.resize(img.reshape((28, 28)), (280, 280)) * 255
        print('Predicted digit: ', predicted_digit)

        # Display the image
        cv2.imshow('Predicted Digit', img_disp)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        # Load the MNIST dataset
        (_, _), (X_test, y_test) = mnist.load_data()

        # Transform the dataset to have values between 0 and 1
        X_test = X_test/255

        # Reshape the dataset to fit the model
        X_test = X_test.reshape((-1, 784))

        # Select 3 random images from the test set
        indices = random.sample(range(X_test.shape[0]), 3)

        for index in indices:
            img = X_test[index]

            # Predict the digit
            prediction = model.predict(img.reshape(1, 784))
            predicted_digit = np.argmax(prediction)

            # Reshape the image for display
            img_disp = img.reshape((28, 28)) * 255

            # Write the predicted digit on the image
            cv2.putText(img_disp, str(predicted_digit), (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
            print('Predicted digit: ', predicted_digit)

            # Display the image
            cv2.imshow('Predicted Digit', img_disp)
            cv2.waitKey(0)

        cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', action='store_true')
    parser.add_argument('--predict', action='store_true')
    parser.add_argument('image_path', nargs='?', default=None)
    args = parser.parse_args()

    if args.train:
        train_model()
    elif args.predict:
        predict_model(args.image_path)
