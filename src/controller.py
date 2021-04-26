from flask import Flask, request
from PIL import Image
import io

from display import Display
from waveshare_epd import epd7in5b_V2

app = Flask(__name__)
display = Display(epd7in5b_V2)


@app.route('/image', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        image_bytes = request.get_data()
        image = Image.open(io.BytesIO(image_bytes))
        display.show_on_hardware(image)

    return ('', 204)


if __name__ == '__main__':
    app.run()
