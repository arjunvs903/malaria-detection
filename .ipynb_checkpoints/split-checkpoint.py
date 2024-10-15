import os
import shutil
import random

# Set the paths for the original dataset, and the new directories for train, val, and test sets
original_dataset_dir = 'datasource/cell_images'
base_dir = 'dataset'
train_dir = os.path.join(base_dir, 'train')
val_dir = os.path.join(base_dir, 'val')
test_dir = os.path.join(base_dir, 'test')

# Set the percentage of data for each set
train_percentage = 0.7
val_percentage = 0.2
test_percentage = 0.1

# Create the new directories for train, val, and test sets
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Loop through each class directory in the original dataset and split the data
for class_dir in os.listdir(original_dataset_dir):
    class_path = os.path.join(original_dataset_dir, class_dir)
    if not os.path.isdir(class_path):
        continue

    # Create the new directories for this class in train, val, and test sets
    os.makedirs(os.path.join(train_dir, class_dir), exist_ok=True)
    os.makedirs(os.path.join(val_dir, class_dir), exist_ok=True)
    os.makedirs(os.path.join(test_dir, class_dir), exist_ok=True)

    # Get the list of all image filenames in this class directory
    all_images = os.listdir(class_path)
    random.shuffle(all_images)

    # Calculate the number of images for each set based on the percentages
    num_images = len(all_images)
    num_train_images = int(num_images * train_percentage)
    num_val_images = int(num_images * val_percentage)
    num_test_images = num_images - num_train_images - num_val_images

    # Copy the images to the corresponding directories in train, val, and test sets
    for i, image_name in enumerate(all_images):
        src_path = os.path.join(class_path, image_name)

        if i < num_train_images:
            dst_dir = os.path.join(train_dir, class_dir)
        elif i < num_train_images + num_val_images:
            dst_dir = os.path.join(val_dir, class_dir)
        else:
            dst_dir = os.path.join(test_dir, class_dir)

        dst_path = os.path.join(dst_dir, image_name)
        shutil.copyfile(src_path, dst_path)