import matplotlib.pyplot as plt
from numpy import argmax
import numpy
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, GlobalAveragePooling2D, Conv2D, Flatten
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import categorical_crossentropy

def load_cifar10():

    (X_train, y_train), (X_test, y_test) = cifar10.load_data()

    '''
    # If you want to play around with the models but don't want to wait
    # for a long time, you can reduce the dataset to 10%. Just don't
    # expect the same accuracies.
    
    X_train = X_train[:5000,:,:,:]
    X_test = X_test[:1000,:,:,:]
    y_train = y_train[:5000,:]
    y_test = y_test[:1000,:]
    '''
    assert X_train.shape == (50000, 32, 32, 3)
    assert X_test.shape == (10000, 32, 32, 3)
    assert y_train.shape == (50000, 1)
    assert y_test.shape == (10000, 1)

    # normalize input data X 
    X_train, X_test = X_train / 255.0, X_test / 255.0
    print(X_train.shape)

    # One-hot encode labels Y
    y_train = to_categorical(y_train,  dtype ="uint8")
    y_test = to_categorical(y_test,  dtype ="uint8")


    print(y_train.shape)

    # Shuffle first (optional)
    idx = numpy.arange(len(X_train))
    numpy.random.shuffle(idx)

    # get first 10% of data
    X_train = X_train[:int(.01*len(idx))]
    y_train = y_train[:int(.01*len(idx))]


    print(y_train.shape)
    print("shape",X_train[0].shape)

    # --------------------------------------------------------------------
    
    return X_train, y_train, X_test, y_test
    
y = load_cifar10()

def create_model():

    inp = Input((32,32,3))# todo: define apropriate input shape

    # todo: implement the hidden layers------------------------------------

    # 1. / 2. hidden layer should be identical 
    x = Conv2D(32, (3, 3), activation='relu' ,strides = (1,1))(inp)
    x = Conv2D(32, (3, 3), activation='relu', strides = (1,1))(x)
  
    x = Flatten()(x)
    print(x.shape)
    
    # last hidden layer i.e.. output layer
    x = Dense(10, activation='softmax')(x)

    # -----------------------------------------------------------------------

    model = Model(inputs=inp, outputs=x)


    # todo: compile the model -----------------------------------------------
    model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
    # -----------------------------------------------------------------------

    return model

def train_model(model, X_train, y_train, X_test, y_test, n_epochs=3):
    
    print(X_train.shape)
    history = model.fit(X_train,
                        y_train,
                        epochs=n_epochs,
                        batch_size = 4,
                        validation_split=0.1,
                       )
    
    return history

def plot_history(his):

    plt.plot(his.history["accuracy"], label = "accuracy")
    plt.plot(his.history["val_accuracy"], label = "val_accuracy")
    plt.legend()
    plt.title("Accuracy")
    plt.show()

    plt.plot(his.history["loss"], label = "loss")
    plt.plot(his.history["val_loss"], label = "val_loss")
    plt.legend()
    plt.title("Loss")
    plt.show()

def main():
    # use this for your own testing!
    #labels = ["airplane", "automobile", "bird", "cat", "deer", 
              #"dog", "frog", "horse", "ship", "truck"]
    X_train, y_train, X_test, y_test = load_cifar10()
    #plt.imshow(X_train[0])
    #plt.gca.set_title("class:" + labels[argmax(y_train[0])])
    #plt.show()
    #print("class:", labels[argmax(y_train[0])])
    
    model = create_model()
    model.summary()


    # feel free to train the model (it might take a while)
    history = train_model(model, X_train, y_train, X_test, y_test, n_epochs=3)
    plot_history(history)

main()