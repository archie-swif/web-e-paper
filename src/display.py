import logging

from PIL import Image

from image_tools import split_to_colors

logger = logging.getLogger('Display')


class Display:
    logging.basicConfig(level=logging.DEBUG)
    waveshare_api = None

    def __init__(self, waveshare_api=None):
        self.waveshare_api = waveshare_api

    def show_on_software(self, image: Image.Image):
        black_image, color_image = split_to_colors(image)
        image.show(title='original')
        black_image.show(title='black')
        color_image.show(title='color')

    def show_on_hardware(self, image: Image.Image):
        epd = self.waveshare_api.EPD()
        epd.init()
        black_image, color_image = split_to_colors(image)

        epd.display(epd.getbuffer(black_image), epd.getbuffer(color_image))

        logging.info("Zzzz...")
        epd.sleep()

    def clear(self):
        if self.waveshare_api:
            self.waveshare_api.init()
            self.waveshare_api.Clear()
