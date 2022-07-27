import random
import os
from preprocessing.preprocess import make_dir, process_path, compare, save_file_from_tftensor, save_label
from preprocessing.augmentation_techniques import rotate, brightness, contrast, occlusion, distortion, blur

def run_augmentation(load_img_path, save_img_path, save_label_path, load_img, generate_number, methods):
    #print(os.path)
    image_names = make_dir(load_img_path, img_type=load_img) # pass *.jpg or *.png
    #print('image_names sample = {}'.format(image_names[0]))

    label_file_path = open(save_label_path, 'w')
    # main loop for augmentation
    for i in range(len(image_names)):
        img, label = process_path(image_names[i])
        #print('img = {} type = {}, label = {}'.format(img.shape, type(img), label))
        # data augmentation
        for j in range(generate_number):
            if 1 in methods:
                augmented_img = rotate(img, degree=random.randint(20, 320)) # rotation
            if 2 in methods:
                augmented_img = occlusion(augmented_img, random.randint(100, 150), random.randint(200, 450),random.randint(100, 200))  # occlusion
            if 3 in methods:
                augmented_img = brightness(augmented_img, max_delta=0.95, seed=(j, 0)) # brightness
            if 4 in methods:
                augmented_img = contrast(augmented_img, 0.4, 0.8, seed=(j,0))  # contrast
            if 5 in methods:
                augmented_img = blur(augmented_img, sigma=random.randint(1, 2)) # blur
            if 6 in methods:
                augmented_img = distortion(augmented_img, distortion_place=random.randint(augmented_img.shape[1] - 10, augmented_img.shape[1])) # distortion
            compare(img, augmented_img)  # compare with original
            save_file_from_tftensor(augmented_img=augmented_img, label='{}.{}.{}'.format(i,j,load_img.split('.')[-1]), save_img_path=save_img_path)
            save_label(label_file_path, label)
        # end

        # save
        #print('before saving type = {}'.format(type(augmented_img)))
        #if i == 0:
            #break
    label_file_path.close()


