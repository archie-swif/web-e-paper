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
        image.show()

    def show_on_hardware(self, image: Image.Image):
        epd = self.waveshare_api.EPD()
        logger.info("Init and Clear")
        epd.init()
        epd.Clear()

        black_image, red_image = split_to_colors(image)

        epd.display(epd.getbuffer(black_image), epd.getbuffer(red_image))

        logging.info("Zzzz...")
        epd.sleep()

    def clear(self):
        if self.waveshare_api:
            self.waveshare_api.init()
            self.waveshare_api.Clear()
