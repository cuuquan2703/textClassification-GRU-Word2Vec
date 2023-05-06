import os
import numpy as np
import json

TRAINING= os.path.abspath("./data/Train_Full")
TESTING= os.path.abspath("./data/Test_Full")
DATA_SET = os.path.abspath("../data")
label = {}
training_data = np.array([])
test_data = np.array([])
valid_data = np.array([])

#Convert file to label
def setLabel():
    label = {category: idx for idx,category in enumerate(os.listdir(TRAINING))}
    return label

def content2label(category,filename):
    with open(os.path.join(TRAINING,category,filename),"r",encoding='utf-16') as _f:
        print(f"Reading {os.path.join(TRAINING,category,filename)}")
        data = _f.read()

    return (data,label[category])

def get_training_data():
    training = np.array([])
    for category in os.listdir(TRAINING):
        path = os.path.join(TRAINING,category)
        for _file in os.listdir(path):
            training = np.append(training,content2label(category,_file))
    
    return  training


label = setLabel()
training_data = get_training_data()
print(training_data[0])
object = {'data':training_data}
json_object = json.dumps(object,indent=4)
with open(os.path.join(DATA_SET,'train.json'),"w",encoding='utf-16') as _f:
    _f.write(json_object)
    
