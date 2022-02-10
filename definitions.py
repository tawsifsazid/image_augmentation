import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
load_img_path = os.path.join(ROOT_DIR, 'data\\images') # load images to start augmenting
save_img_path = os.path.join(ROOT_DIR, 'data\\augmented\\images') # save augmented images
save_label_path = os.path.join(ROOT_DIR, 'data\\augmented\\labels\\labels.txt') # save labels for the augmented images

