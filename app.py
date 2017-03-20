import datetime
import picamera
from flask import Flask, send_file

app = Flask(__name__)

camera = picamera.PiCamera()
camera.vflip = True
camera.hflip = True

@app.route('/')
def take_photo(identifier=datetime.datetime.now().isoformat):
    photo = 'photos/' + identifier + '.jpg'
    camera.capture(photo)
    return send_file(photo)

if __name__ == '__main__':
    app.run(host='10.0.0.22', port=2222)
