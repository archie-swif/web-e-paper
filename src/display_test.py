import logging

from display import Display
from PIL import Image, ImageDraw, ImageFont

from image_tools import split_to_colors

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Test')


from waveshare_epd import epd2in13bc

#display = Display(epd2in13bc)

image = Image.new('RGB', (212, 104), (255,255,255))  # 255: clear the frame
image_draw = ImageDraw.Draw(image)
font = ImageFont.truetype("img/Perfect DOS VGA 437.ttf", 40)
image_draw.text((10, 10), "Hello", font=font, fill=0)
image_draw.text((10, 50), "WORLD", font=font, fill=(255,0,0))
display = Display(epd2in13bc)
display.show_on_hardware(image)

#epd = epd2in13bc.EPD()
#epd.init()
#epd.display(epd.getbuffer(image), epd.getbuffer(image))
