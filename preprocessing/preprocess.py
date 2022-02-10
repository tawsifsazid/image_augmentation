import os
import tensorflow as tf
import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, array_to_img

def read_label(path):
    with open(path, 'r') as f:
        a = f.readlines()
    return a

def save_label(file, label):
    file.write('{}\n'.format(label))

def save_file_from_tftensor(augmented_img, label, save_img_path):
    tf.keras.preprocessing.image.save_img('{}/{}'.format(save_img_path, label), augmented_img, scale=False)

def compare(original, augmented):
    fig = plt.figure()
    plt.subplot(1,2,1)
    plt.title('Original image')
    plt.imshow(original)

    plt.subplot(1,2,2)
    plt.title('Augmented image')
    plt.imshow(augmented)
    plt.show()

def show_img(img): # we can give raw path to view the image
    plt.imshow(mpimg.imread(img))
    plt.show()

def make_dir(path, img_type):
    list_of_files = glob.glob(os.path.join(path, img_type))
    return list_of_files

def get_label(path):
    label = path.split('\\')[-1].split('.')[0] # not using tf string tensor
    return label

def decode_img(img):
    # convert the compressed string to a 3D uint8 tensor
    img = tf.image.decode_png(img, channels=0)
    return img

def resize(img, size):
    return tf.image.resize(img, [size, size])

def process_path(path):
    label = get_label(path) # fetch label

    img = tf.io.read_file(path)
    img = decode_img(img) # image decode
    return img, label



