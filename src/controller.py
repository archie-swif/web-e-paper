from PIL import Image, ImageDraw, ImageFont
from flask import Flask, request
import io

from display import Display

# from waveshare_epd import xepd2in13bc
from waveshare_epd import epd7in5b_HD

app = Flask(__name__)
# display = Display(epd2in13bc)
display = Display(epd7in5b_HD)


# display = Display()


@app.route('/image', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        file = Image.open(request.files['image'])
        file = file.convert(mode="RGB", dither=False)
        image = Image.new('RGB', (880, 528), (255, 255, 255))  # 255: clear the frame
        image.paste(file)
        image = image.transpose(method=Image.ROTATE_180)
        display.show_on_hardware(image)
    return ('', 204)


@app.route('/text', methods=['POST'])
def upload_text():
    if request.method == 'POST':
        text = request.data.decode("utf-8")
        text_size = int(request.args.get('size')) | 16
        image = Image.new('RGB', (800, 480), (255, 255, 255))  # 255: clear the frame

        draw = ImageDraw.Draw(image)
        draw.fontmode = "1"  # Color mode bin / greyscale
        font = ImageFont.truetype("img/VGA_8x16.ttf", size=text_size)
        draw.multiline_text((0, 0), text, font=font, fill=(255, 0, 0))
        image = image.transpose(method=Image.ROTATE_180)
        display.show_on_hardware(image)
    return ('', 204)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
