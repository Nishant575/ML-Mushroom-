import pickle
import json
import numpy as np

__attributes = None
__model = None
__encoder = None

    
def detect(data2):
    data = ['p']
    data.extend(data2)
    new_data = np.array(data).reshape(1, -1)
    new_data = __encoder.transform(new_data)
    new_data = np.delete(new_data[0],0)
    pred = __model.predict(new_data.reshape(1, -1))
    if pred[0] == 1.0:
        return "Mushroom is poisonous",1
    else:
        return "Mushroom is edible",0

def get_att():
    return __attributes


def load_saved_artifacts():
    global __attributes
    
    with open("artifacts/attributes.json", "r") as f:
        
        __attributes = json.load(f)
    
        
    global __model
    if __model is None:
        with open("artifacts/mushroom_model2.pickle",'rb') as f:
            
            __model = pickle.load(f)
    
    global __encoder
    if __encoder is None:
        
        with open("artifacts/encoding2.pkl", 'rb') as f:
            
            __encoder = pickle.load(f)
    
load_saved_artifacts()
