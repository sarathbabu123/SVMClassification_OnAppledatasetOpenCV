import pandas as pd
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os
import pickle
import random
from sklearn.svm import SVC

### Making the train data file and saving in pickle file
# dir = "../SVM_Classification/Datasetcombine/train"

# categories = os.listdir(dir)
# data = []

# for category in categories:
#     path = os.path.join(dir,category)
#     label = categories.index(category)
    
#     for img in os.listdir(path):
#         imgpath = os.path.join(path,img)
#         appleimg = cv.imread(imgpath,0)
#         appleimg = cv.resize(appleimg,(100,100))
#         img  = np.array(appleimg).flatten()
#         data.append([img,label])


# pick_in = open('data0.pickle','wb')
# pickle.dump(data,pick_in)
# pick_in.close


### Making the test data and saving it on pickle file

# dir = "../SVM_Classification/Datasetcombine/test"

# categories = os.listdir(dir)
# data = []
# for category in categories:
#     path = os.path.join(dir,category)
#     label = categories.index(category)
    
#     for img in os.listdir(path):
#         imgpath = os.path.join(path,img)
#         appleimg = cv.imread(imgpath,0)
#         appleimg = cv.resize(appleimg,(100,100))
#         img  = np.array(appleimg).flatten()
#         data.append([img,label])
        
# pick_in = open('testdata.pickle','wb')
# pickle.dump(data,pick_in)
# pick_in.close

