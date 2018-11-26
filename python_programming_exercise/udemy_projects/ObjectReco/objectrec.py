from keras.datasets import cifar10
from keras.utils import np_utils 
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

(X_train,y_train),(X_test,y_test)=cifar10.load_data()
print('Training Images {}'.format(X_train.shape))
print('Testing Images {}'.format(X_test.shape))

# print(X_train[0].shape)
# create a grid of 3x3 images
for i in range(0,9):
    plt.subplot(330+1 +i)
    img = X_train[50+i]
    plt.imshow(img)
    
# show the plot
plt.show()

#Prepositing the dataset
seed=6
np.random.seed(seed)

(X_train,y_train),(X_test,y_test)=cifar10.load_data()

X_train=X_train.astype('float32')
X_test=X_test.astype('float32')

X_train/=255.0
X_test/=255.0
# print(X_train[0])

print(y_train.shape)
print(y_train[0])

#[6]=[0,0,0,0,0,0,1,0,0,0]

#hot encoder output
y_train=np_utils.to_categorical(y_train)
y_test= np_utils.to_categorical(y_test)

num_class=y_test.shape[1]
print(num_class)
print(y_train[0])

#Bulding the ALL-CNN
from keras.models import Sequential
from keras.layers import Dropout,Activation,Conv2D,GlobalAveragePooling2D
from keras.optimizers import SGD

#define the model

def allcnn(weights=None):
    model=Sequential()

    model.add(Conv2D(96,(3,3),padding='same',input_shape=(32,32,3)))
    model.add(Activation('relu'))
    model.add(Conv2D(96,(3,3),padding='same'))
    model.add(Activation('relu'))
    model.add(Conv2D(96,(3,3),padding='same',strides=(2,2)))
    model.add(Dropout(0,5))

    model.add(Conv2D(192,(3,3),padding='same'))
    model.add(Activation('relu'))
    model.add(Conv2D(192,(3,3),padding='same'))
    model.add(Activation('relu'))
    model.add(Conv2D(192,(3,3),padding='same',strides=(2,2)))
    model.add(Dropout(0,5))

    model.add(Conv2D(192,(3,3),padding='same'))
    model.add(Activation('relu'))
    model.add(Conv2D(192,(1,1),padding='valid'))
    model.add(Activation('relu'))
    model.add(Conv2D(10,(1,1),padding='valid'))

#add Global 
    model.add(GlobalAveragePooling2D())
    model.add(Activation('softmax'))

    if weights:
        model.load_weights(weights)

    return model

#define hyper parameters
learning_rate=0.01
weight_decay=1e-6
momentum=0.9

#build model
model=allcnn()

#define optimizer and compile model 
sgd=SGD(lr=learning_rate,momentum=momentum,decay=weight_decay,nesterov=True)
model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['accuracy'])

#print model summary
print(model.summary())