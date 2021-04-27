import numpy as np
from PIL import Image


def split_to_colors(image):
    data = np.array(image)
    red, green, blue = data[:, :, 0], data[:, :, 1], data[:, :, 2]
    color_mask = ((red > 10) | (green > 10) ) & (blue < 10)
    black_mask = (red + green + blue == 0)

    color_data = data.copy()
    color_data[color_mask] = [0, 0, 0]
    color_data[black_mask] = [255, 255, 255]
    color_image = Image.fromarray(color_data).convert(mode="1", dither=False)

    data[color_mask] = [255, 255, 255]
    black_image = Image.fromarray(data).convert(mode="1", dither=False)
    return black_image, color_image
