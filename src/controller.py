from PIL import Image, ImageDraw, ImageFont
from flask import Flask, request
import io

from display import Display

from waveshare_epd import epd2in13bc

app = Flask(__name__)
display = Display(epd2in13bc)
# display = Display()


@app.route('/image', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        image_bytes = request.get_data()
        file = Image.open(io.BytesIO(image_bytes))
        file = file.convert(mode="RGB", dither=False)
        image = Image.new('RGB', (212, 104), (0, 0, 0))  # 255: clear the frame
        image.paste(file)
        display.show_on_hardware(image)
    return ('', 204)


@app.route('/text', methods=['POST'])
def upload_text():
    if request.method == 'POST':
        text = request.data.decode("utf-8")
        text_size = int(request.args.get('size')) | 16
        image = Image.new('RGB', (212, 104), (255, 255, 255))  # 255: clear the frame

        draw = ImageDraw.Draw(image)
        draw.fontmode = "1"  # Color mode bin / greyscale
        font = ImageFont.truetype("img/DOS437.ttf", size=text_size)
        draw.multiline_text((0, 0), text, font=font, fill=(0, 0, 0))
        display.show_on_hardware(image)
    return ('', 204)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
