import tensorflow as tf
from tensorflow.keras import layers, models

def main():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    x_train = (x_train / 255.0).astype("float32")[..., None]
    x_test  = (x_test / 255.0).astype("float32")[..., None]

    model = models.Sequential([
        layers.Input(shape=(28, 28, 1)),
        layers.Conv2D(32, (3, 3), activation="relu"),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation="relu"),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation="relu"),
        layers.Dropout(0.3),
        layers.Dense(10, activation="softmax")
    ])

    model.compile(optimizer="adam",
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])

    model.summary()
    model.fit(x_train, y_train, validation_split=0.1, epochs=3, batch_size=128)

    test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
    print(f"Test Accuracy: {test_acc:.4f}")

    model.save("mnist_cnn_model.keras")
    print("Saved: mnist_cnn_model.keras")

if __name__ == "__main__":
    main()
