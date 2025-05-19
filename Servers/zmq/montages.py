import numpy as np
import cv2


def build_montages(image_list, image_shape, montage_shape):
    if len(image_shape) != 2:
        raise Exception('image shape must be list or tuple of length 2 (rows, cols)')
    if len(montage_shape) != 2:
        raise Exception('montage shape must be list or tuple of length 2 (rows, cols)')
    image_montages = []
    montage_image = np.zeros(
        shape=(image_shape[1] * (montage_shape[1]), image_shape[0] * montage_shape[0], 3),
        dtype=np.uint8)
    cursor_pos = [0, 0]
    start_new_img = False
    for img in image_list:
        if type(img).__module__ != np.__name__:
            raise Exception(f'input of type {type(img)} is not a valid numpy array')
        start_new_img = False
        img = cv2.resize(img, image_shape)
        montage_image[cursor_pos[1]:cursor_pos[1] + image_shape[1], cursor_pos[0]:cursor_pos[0] + image_shape[0]] = img
        cursor_pos[0] += image_shape[0]
        if cursor_pos[0] >= montage_shape[0] * image_shape[0]:
            cursor_pos[1] += image_shape[1]
            cursor_pos[0] = 0
            if cursor_pos[1] >= montage_shape[1] * image_shape[1]:
                cursor_pos = [0, 0]
                image_montages.append(montage_image)
                montage_image = np.zeros(
                    shape=(image_shape[1] * (montage_shape[1]), image_shape[0] * montage_shape[0], 3),
                    dtype=np.uint8)
                start_new_img = True
    if start_new_img is False:
        image_montages.append(montage_image)
    return image_montages
