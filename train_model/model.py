from keras.applications.mobilenet import MobileNet
from keras.applications.mobilenet_v2 import MobileNetV2
import efficientnet.keras as efn
from keras.applications.resnet50 import ResNet50
from keras.applications.vgg16 import VGG16
from keras.models import Sequential
from keras.layers import Activation
from keras.layers import Input, Dropout
from keras.layers import Dense, GlobalAveragePooling2D
from keras.models import Model
from keras.optimizers import SGD
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
from keras.preprocessing.image import load_img,img_to_array,ImageDataGenerator,array_to_img

class Generator_train(object): # rule1
    def __init__(self):

        train_dir="./train_data"
        datagen = ImageDataGenerator(zoom_range=[0.95, 1.0],width_shift_range = 0.05, height_shift_range=0.05,brightness_range=[0.95, 1.05], rescale=1/255.)

        train_gen = datagen.flow_from_directory(
            train_dir,
            target_size=(50,50),
            batch_size=32,
            class_mode='categorical',
            shuffle=True,
            subset = "training" 
        )
        
        self.gene = train_gen
        
    def __iter__(self):
        return self
    
    def __next__(self): 
        X, Y = self.gene.next()
        return [X,Y], Y

class Generator_val(object): # rule1
    def __init__(self):

        val_dir="./val_data"
        datagen = ImageDataGenerator(zoom_range=[0.95, 1.0],width_shift_range = 0.05, height_shift_range=0.05,brightness_range=[0.95, 1.05], rescale=1/255.)

        val_gen = datagen.flow_from_directory(
            val_dir,
            target_size=(50,50),
            batch_size=32,
            class_mode='categorical',
            shuffle=True,
            subset = "training" 
        )
        
        self.gene = val_gen
        
    def __iter__(self):
        return self
    
    def __next__(self): 
        X, Y = self.gene.next()
        return [X,Y], Y

def main():
    train_generator=Generator_train()
    val_generator=Generator_val()
    # model = model()
    n_categories=2
    base_model=VGG16(input_shape=(50,50,3),
                        weights="imagenet",
                        include_top=False)

    x = base_model.output
    yinput = Input(shape=(n_categories,))
    hidden = GlobalAveragePooling2D()(x)
    x = Dropout(0.5)(hidden)
    x = Dense(1024,activation='relu')(x)
    x = Dense(512,activation='relu')(x)
    x = Dense(256,activation='relu')(x)
    x = Dense(2,activation='relu')(x)
    prediction = Activation('softmax' , name="act_softmax")(x)
    learn_model = Model(inputs=[base_model.input,yinput],outputs=prediction)

    for layer in base_model.layers[:15]:
        layer.trainable = False

    learn_model.compile(optimizer=Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
    learn_model.summary()

    learn_model.fit_generator(train_generator, steps_per_epoch=10, epochs=100, verbose=1, validation_data=val_generator, validation_steps=10, class_weight=None, max_queue_size=10, workers=1, use_multiprocessing=False, shuffle=True, initial_epoch=0)
    learn_model.save('train_weights.h5')

if __name__ == "__main__":
    main()