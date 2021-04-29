from keras.models import load_model
import os
from pathlib import  Path


model = load_model(os.path.join(Path(__file__).parent , 'cnnCat2.h5'))

def predict(Eye):
    if Eye is None:
        # eyes are not detected so effectively we can consider this case as drowsy
        return 0
    return model.predict_classes(Eye)[0]


