from PIL import Image, ImageDraw, ImageFont
from flask import Flask, request, render_template
import io

from display import Display
from waveshare_epd import epd7in5b_HD

app = Flask(__name__)
# display = Display(epd2in13bc)
# display = Display()
display = Display(epd7in5b_HD)


@app.route('/')
def index():
    return render_template('index.html')

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
        text = request.form['text'].replace('\r','')
        print(repr(text))
        text_size = int(request.values.get('size'))| 16
        image = Image.new('RGB', (880, 528), (255, 0, 0))  # 255: clear the frame

        draw = ImageDraw.Draw(image)
        draw.fontmode = "1"  # Color mode bin / greyscale
        font = ImageFont.truetype("img/Pixel-UniCode.ttf", size=text_size)
        draw.multiline_text((2, 2), text, font=font, fill=(0, 0, 0))
        draw.multiline_text((0, 0), text, font=font, fill=(255, 255, 255))
        image = image.transpose(method=Image.ROTATE_180)
        display.show_on_hardware(image)
    return ('', 204)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
