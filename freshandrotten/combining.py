import os
import shutil

# Source directory containing subfolders
source_dir = '../SVM_Classification/Dataset/Test'

# # List of folders to combine
# folders_to_combine = ['apple_6', 'apple_braeburn_1', 'apple_crimson_snow_1', 'apple_golden_1', 'apple_golden_2',
#                       'apple_golden_3', 'apple_granny_smith_1', 'apple_pink_lady_1', 'apple_red_1',
#                       'apple_red_2', 'apple_red_3', 'apple_red_delicios_1', 'apple_red_yellow_1']

# List of folders to combine
folders_to_combine = ['apple_hit_1','apple_rotten_1']

# Destination directory for combined images
destination_dir = '../SVM_Classification/Datasetcombine/test/RottenApples'

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
