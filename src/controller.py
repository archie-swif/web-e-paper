import base64
import io
import logging

from PIL import Image, ImageDraw, ImageFont
from flask import Flask, request, render_template, redirect, url_for

from display import Display
from waveshare_epd import epd7in5b_HD

app = Flask(__name__)
# display = Display(epd2in13bc)
# display = Display()
display = Display(epd7in5b_HD)
text = ''
image_data = 'data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs='


@app.route('/')
def index():
    return render_template('index.html', text=text)


@app.route('/image', methods=['GET'])
def image():
    return render_template('image.html', image_data=image_data)


@app.route('/image', methods=['POST'])
def upload_image():
    global image_data
    file = request.files['image']
    file = Image.open(file)

    PALETTE = [
                  0, 0, 0,  # black,  00
                  128, 28, 28,  # red,    10
                  255, 255, 255,  # yellow, 11
              ] + [0, ] * 252 * 3
    pimage = Image.new("P", (1, 1), 0)
    pimage.putpalette(PALETTE)


    file = file.convert(mode="RGB", dither=False)
    file.thumbnail((528, 880), resample=Image.BICUBIC, reducing_gap=2.0)
    # file = file.quantize(palette=pimage, dither=Image.FLOYDSTEINBERG)
    image = Image.new('RGB', (528, 880), (255, 255, 255))  # 255: clear the frame
    image.paste(file)

    with io.BytesIO() as buf:
        image.save(buf, 'png')
        image_bytes = buf.getvalue()
    image_data = "data:image/jpeg;base64,"+base64.b64encode(image_bytes).decode()

    image = image.transpose(method=Image.ROTATE_180)
    display.show_on_hardware(image)
    return redirect(url_for('image'))


@app.route('/text', methods=['POST'])
def upload_text():
    global text
    if request.method == 'POST':
        text = request.form['text'].replace('\r', '')
        logging.info(text)
        text_size = int(request.values.get('size')) | 16
        image = Image.new('RGB', (528, 880), (255, 0, 0))  # 255: clear the frame

        draw = ImageDraw.Draw(image)
        draw.fontmode = "1"  # Color mode bin / greyscale
        font = ImageFont.truetype("./src/static/vga.ttf", size=text_size)
        draw.multiline_text((2, 2), text, font=font, fill=(0, 0, 0))
        draw.multiline_text((0, 0), text, font=font, fill=(255, 255, 255))
        #image = image.transpose(method=Image.ROTATE_180)
        display.show_on_hardware(image)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
