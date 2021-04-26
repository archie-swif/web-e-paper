import logging


class EPD:

    def __init__(self, width=800, height=480):
        self.width = width
        self.height = height

    # Hardware reset
    def reset(self):
        logging.info("RESET")

    def send_data(self, data):
        logging.debug("SEND DATA " + data)

    def init(self):
        return 0

    def getbuffer(self, image):
        buf = [0xFF] * (int(self.width / 8) * self.height)
        image_monocolor = image.convert('1')
        imwidth, imheight = image_monocolor.size
        pixels = image_monocolor.load()
        logging.debug('imwidth = %d  imheight =  %d ', imwidth, imheight)
        if (imwidth == self.width and imheight == self.height):
            logging.debug("Horizontal")
            for y in range(imheight):
                for x in range(imwidth):
                    # Set the bits for the column of pixels at the current position.
                    if pixels[x, y] == 0:
                        buf[int((x + y * self.width) / 8)] &= ~(0x80 >> (x % 8))
        elif (imwidth == self.height and imheight == self.width):
            logging.debug("Vertical")
            for y in range(imheight):
                for x in range(imwidth):
                    newx = y
                    newy = self.height - x - 1
                    if pixels[x, y] == 0:
                        buf[int((newx + newy * self.width) / 8)] &= ~(0x80 >> (y % 8))
        return buf

    def display(self, imageblack, imagered):
        COLOR_YELLOW = (255, 0, 0)

        color_img = imageblack.convert('RGB')

        width, height = imageblack.size
        for y in range(height):
            for x in range(width):
                if imagered.getpixel((x, y)) == 0:
                    color_img.putpixel((x, y), (255, 0, 0))

        color_img.show()

    def Clear(self):
        logging.info("CLEAR")

    def sleep(self):
        logging.info("SLEEP")
