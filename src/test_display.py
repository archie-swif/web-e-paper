import logging

from display import Display
from PIL import Image, ImageDraw, ImageFont

from image_tools import split_to_colors

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Test')


def test_image_split_by_color():
    image = Image.new('RGB', (800, 480), (255, 255, 255))  # 255: clear the frame
    draw = ImageDraw.Draw(image)
    draw.line((140, 75, 190, 75), fill=0)
    draw.arc((140, 50, 190, 100), 0, 360, fill=0)
    draw.rectangle((80, 50, 130, 100), fill=(0, 0, 0))
    draw.chord((200, 50, 250, 100), 0, 360, fill=(255, 0, 0))

    black, color = split_to_colors(image)

    black.show()
    color.show()


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
    from waveshare_epd import epd2in13bc
    display = Display(epd2in13bc)

    image = Image.new('RGB', (250, 122), (0, 0, 0))  # 255: clear the frame
    image_draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("img/Perfect DOS VGA 437.ttf", 40)
    image_draw.text((10, 10), "Hello", font=font, fill=(255, 0, 0))
    image_draw.text((10, 50), "WORLD", font=font, fill=(255, 255, 255))
    display.show_on_hardware(image)
