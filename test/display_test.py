import logging
import time

from display import Display
from PIL import Image, ImageDraw, ImageFont

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Test')


def test_show_image_on_software():
    display = Display()

    image = Image.new('RGB', (800, 480), (255, 255, 255))  # 255: clear the frame
    draw_Himage = ImageDraw.Draw(image)
    draw_Himage.line((140, 75, 190, 75), fill=0)
    draw_Himage.arc((140, 50, 190, 100), 0, 360, fill=0)
    draw_Himage.rectangle((80, 50, 130, 100), fill=(0, 0, 0))
    draw_Himage.chord((200, 50, 250, 100), 0, 360, fill=(255, 0, 0))
    display.show_on_software(image)


def test_show_image_on_hardware():
    display = Display()

    image = Image.new('RGB', (250, 122), (255, 255, 255))  # 255: clear the frame
    image_draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("img/Perfect DOS VGA 437.ttf", 40)
    image_draw.text((10, 10), "Hello", font=font, fill=(255, 0, 0))
    image_draw.text((10, 50), "WORLD", font=font, fill=(0, 0, 0))
    display.show_on_software(image)
