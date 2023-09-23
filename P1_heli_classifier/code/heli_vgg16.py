from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Dense, Flatten, BatchNormalization, Activation
from tensorflow.keras.optimizers import Adam

from tensorflow.keras.applications import VGG16
import numpy as np
from myloc import loader3
import csv

def label_load(path):
    file=open(path)
    labeldata=csv.reader(file)
#     label_list=np.eye(2)[np.array([i for i in labeldata]).astype(int)]
#     label=label_list.reshape(-1,2) # 3차원을 2차원으로 변경
    label=np.array([i for i in labeldata]).astype(int)
    return label

batch_size = 28
num_classes = 2
epochs = 30

y_train = 'c:\\ddata\\cnnmodel\\tr.csv'
y_test = 'c:\\ddata\\cnnmodel\\te.csv'
train_images =  'c:\\ddata\\cnnmodel\\tr'
test_images =  'c:\\ddata\\cnnmodel\\te'

x_train = loader3.image_load(train_images)
y_train = label_load(y_train)
x_test = loader3.image_load(test_images)
y_test = label_load(y_test)       

# #2. 데이터 증식시키기 

# from tensorflow.keras.preprocessing.image import ImageDataGenerator

# train_datagen = ImageDataGenerator(horizontal_flip = True,
#                                    zoom_range = 0.2,
#                                    width_shift_range = 0.1,
#                                    height_shift_range = 0.1,
#                                    rotation_range = 30,
#                                    fill_mode = 'nearest')

# val_datagen = ImageDataGenerator()

# batch_size = 32

# train_generator = train_datagen.flow(x_train, y_train,
#                                     batch_size = batch_size)

# val_generator = val_datagen.flow(x_val, y_val,
#                                 batch_size = batch_size)

# #3. 사전 학습된 모델 사용하기 


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Dense, Flatten, BatchNormalization, Activation
from tensorflow.keras.optimizers import Adam

from tensorflow.keras.applications import VGG16

# imagenet을 학습한 모델을 불러옵니다.
vgg16 = VGG16(weights = None, input_shape = (32, 32, 3), include_top = False)
#vgg16.summary()


#4. 모델 동결해제하기

# # 끝의 4개의 층만 동결을 해제합니다.
# for layer in vgg16.layers[:-4]:
#     layer.trainable = False


#5. 모델 구성학습하기 

model = Sequential()
# vgg16 모델을 사용합니다.
model.add(vgg16)
# 분류기를 직접 정의합니다.
model.add(Flatten())
model.add(Dense(256))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Dense(2, activation = 'softmax'))

# model.summary() # 모델의 구조를 확인하세요!

model.compile(optimizer = Adam(1e-4),
             loss = 'sparse_categorical_crossentropy',
             metrics = ['acc'])

x_train = x_train.astype('float32')
x_test= x_test.astype('float32')
x_train /= 255
x_test /= 255

hist = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=epochs, batch_size=batch_size, verbose=2)
 
# 모델 평가
scores = model.evaluate(x_test, y_test, verbose=0)
print("CNN Error: %.2f%%" % (100-scores[1]*100)) #[ 오차, 정확도 ]
 
# save_model(model, "d:\\ddata\\Heli.h5")

#%%

print(os.listdir('c:\\ddata\\cnnmodel\\tr'))