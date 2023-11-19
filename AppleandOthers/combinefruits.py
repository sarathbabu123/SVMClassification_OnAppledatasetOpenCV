import os
import shutil
import pandas as pd
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import pickle
import random
from sklearn.svm import SVC

## Making the train data file and saving in pickle file
source_dir = "../freshandrotten/Dataset/Test"

categories = os.listdir(source_dir)

print(categories)

# List of folders to combine
# folders_to_combine = ['apple_6', 'apple_braeburn_1', 'apple_crimson_snow_1', 'apple_golden_1', 'apple_golden_2', 'apple_golden_3', 'apple_granny_smith_1', 'apple_hit_1', 'apple_pink_lady_1', 'apple_red_1', 'apple_red_2', 'apple_red_3', 'apple_red_delicios_1', 'apple_red_yellow_1', 'apple_rotten_1']

# List of folders to combine
folders_to_combine = ['cabbage_white_1', 'carrot_1', 'cucumber_1', 'cucumber_3', 'eggplant_violet_1', 'pear_1', 'pear_3', 'zucchini_1', 'zucchini_dark_1']

# Destination directory for combined images
destination_dir = '../AppleandOthers/Combinedataset/Testing/Otherfruits'

# Create destination directory if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Loop through each folder and copy images to the destination folder
for folder in folders_to_combine:
    folder_path = os.path.join(source_dir, folder)
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        shutil.copy(file_path, destination_dir)

print("Images have been combined into the 'apples' folder.")
