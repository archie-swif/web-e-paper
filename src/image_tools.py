import numpy as np
from PIL import Image


def split_to_colors(image):
    data = np.array(image)
    red, green, blue = data[:, :, 0], data[:, :, 1], data[:, :, 2]

    color_image = (red > 10) | (green > 10) & (blue < 10)
    color_data = data.copy()
    color_data[color_image] = [255, 255, 255]
    color_image = Image.fromarray(color_data)

    black_mask = (red < 10) & (green < 10) & (blue < 10)
    data[black_mask] = [255, 255, 255]
    black_image = Image.fromarray(data)
    return black_image, color_image
