import base64

from PIL import Image, ImageDraw, ImageFont
from flask import Flask, request, render_template
import io

from display import Display
from waveshare_epd import epd7in5b_HD

app = Flask(__name__)
# display = Display(epd2in13bc)
# display = Display()
display = Display(epd7in5b_HD)
text = ''


@app.route('/')
def index():
    return render_template('index.html', text=text)


@app.route('/image', methods=['GET'])
def index():
    return render_template('image.html', text=text)


@app.route('/image', methods=['POST'])
def upload_image():
    file = Image.open(request.files['image'])
    file = file.convert(mode="RGB", dither=False)
    image = Image.new('RGB', (880, 528), (255, 255, 255))  # 255: clear the frame
    image.paste(file)
    # image = image.transpose(method=Image.ROTATE_180)
    display.show_on_hardware(image)

    with io.BytesIO() as buf:
        image.save(buf, 'png')
        image_bytes = buf.getvalue()
    encoded_string = base64.b64encode(image_bytes).decode()

    return render_template('image.html', img_data=encoded_string), 200


@app.route('/text', methods=['POST'])
def upload_text():
    global text
    if request.method == 'POST':
        text = request.form['text'].replace('\r', '')
        print(text)
        text_size = int(request.values.get('size')) | 16
        image = Image.new('RGB', (880, 528), (255, 0, 0))  # 255: clear the frame

        draw = ImageDraw.Draw(image)
        draw.fontmode = "1"  # Color mode bin / greyscale
        font = ImageFont.truetype("img/PxPlus_IBM_VGA_8x16.ttf", size=text_size)
        draw.multiline_text((2, 2), text, font=font, fill=(0, 0, 0))
        draw.multiline_text((0, 0), text, font=font, fill=(255, 255, 255))
        image = image.transpose(method=Image.ROTATE_180)
        display.show_on_hardware(image)
    return ('', 204)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
