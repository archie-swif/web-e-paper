from datetime import datetime
import logging
import unittest

from display import Display
from PIL import Image, ImageDraw, ImageFont

from image_tools import split_to_colors

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Test')


class TestDisplay(unittest.TestCase):
    def test_image_split_by_color(self):
        image = Image.new('RGB', (212, 104), (255, 255, 255))  # 255: clear the frame
        draw = ImageDraw.Draw(image)
        draw.fontmode = "1"  # Color mode bin / greyscale
        font = ImageFont.truetype("../img/DOS437.ttf", 40)
        draw.text((10, 0), "Hello", font=font, fill=(255, 0, 0))
        draw.text((10, 50), "World", font=font, fill=(0, 0, 0))

        image.transpose(method=Image.ROTATE_180)

        black, color = split_to_colors(image)

        image.show()
        black.show()
        color.show()

    def test_show_image_on_software(self):
        display = Display()

        image = Image.new('RGB', (212, 104), (0, 0, 0))  # 255: clear the frame
        draw = ImageDraw.Draw(image)
        draw.fontmode = "1"  # Color mode bin / greyscale
        font = ImageFont.truetype("../img/DOS437.ttf", 64)
        draw.text((10, 0), "HELLO", font=font, fill=(255, 255, 255))
        draw.text((10, 50), "WORLD", font=font, fill=(255, 0, 0))
        # image = image.transpose(method=Image.ROTATE_180)
        display.show_on_software(image)


    def test_show_image_on_hardware(self):
        from waveshare_epd import epd2in13bc
        display = Display(epd2in13bc)
        # display = Display()

        image = Image.new('RGB', (212, 104), (0, 0, 0))  # 255: clear the frame
        draw = ImageDraw.Draw(image)
        draw.fontmode = "1"  # Color mode bin / greyscale
        font = ImageFont.truetype("../img/DOS437.ttf", 64)
        draw.text((10, 0), "HELLO", font=font, fill=(255, 255, 255))
        draw.text((10, 50), "WORLD", font=font, fill=(255, 0, 0))
        image = image.transpose(method=Image.ROTATE_180)
        display.show_on_hardware(image)

    def test_show_time(self):
        # from waveshare_epd import epd2in13bc
        # display = Display(epd2in13bc)
        display = Display()

        image = Image.new('RGB', (212, 104), (0, 0, 0))  # 255: clear the frame
        draw = ImageDraw.Draw(image)
        draw.fontmode = "1"  # Color mode bin / greyscale
        font = ImageFont.truetype("../img/DOS437.ttf", 64)
        draw.text((19, 19), datetime.now().strftime("%H:%M"), font=font, fill=(255, 255, 255))
        draw.text((20, 20), datetime.now().strftime("%H:%M"), font=font, fill=(0, 0, 0))
        # image = image.transpose(method=Image.ROTATE_180)
        image.show()

