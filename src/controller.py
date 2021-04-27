from PIL import Image
from flask import Flask, request
import io

from display import Display
from waveshare_epd import epd7in5b_V2

app = Flask(__name__)
display = Display(epd7in5b_V2)


@app.route('/image', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        image_bytes = request.get_data()
        file = Image.open(io.BytesIO(image_bytes))
        file = file.convert(mode="RGB", dither=False)
        image = Image.new('RGB', (212, 104), (0, 0, 0))  # 255: clear the frame
        image.paste(file)
        display.show_on_software(image)
    return ('', 204)


if __name__ == '__main__':
    app.run()
