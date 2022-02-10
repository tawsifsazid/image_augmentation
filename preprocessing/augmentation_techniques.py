import tensorflow as tf
import numpy as np
import scipy
from scipy.ndimage.interpolation import rotate
from PIL import Image

def rotate(img, degree):
    img = scipy.ndimage.rotate(img, degree)  # 1 rad  = 57.2958 degree
    return img

def brightness(img, max_delta, seed):
    img = tf.image.stateless_random_brightness(img, max_delta, seed=seed)
    return img

def contrast(img, lower, upper, seed):
    img = tf.image.stateless_random_contrast(img, lower=lower, upper=upper, seed=seed)
    return img

def occlusion(img, top_left_x, top_left_y, patch_size):
    patched_image = np.array(img, copy=True)
    patched_image[top_left_y:top_left_y + patch_size, top_left_x:top_left_x + patch_size, :] = 127.5
    #print('occlusion type = {}'.format(type(patched_image)))
    return patched_image

def distortion(img, distortion_place):
    image = np.array(img, copy=True)
    cols = image.shape[1]
    rows = image.shape[0]
    #print('cols = {}, rows = {}'.format(rows, cols))
    A = image.shape[0] / 3.0
    w = 0.50 / img.shape[1]
    shift = lambda x: A * np.sin(2.0 * np.pi * x * w)
    for i in range(distortion_place):
        image[:, i] = np.roll(image[:, i], int(shift(i)))
    return image

def blur(img, sigma):
    from scipy.ndimage.filters import gaussian_filter
    img = gaussian_filter(img, sigma=sigma)
    return img
