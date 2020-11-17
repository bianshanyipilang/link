import keras
from keras.models import load_model
from keras.utils import CustomObjectScope
with CustomObjectScope({'DenseFeatures': DenseFeatures}):
    model=load_model('C:/Users/10341/Desktop/ddjin/my_model.h5')
#model = load_model('C:/Users/10341/Desktop/ddjin/my_model.h5', custom_objects={'DenseFeatures': DenseFeatures})
#new_model = keras.models.load_model('C:/Users/10341/Desktop/ddjin/my_model.h5',custom_objects={'feature_layer': feature_layer})