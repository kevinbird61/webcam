#!/usr/bin/env python

from flask import Flask, request, render_template, Response, make_response
from camera import VideoCamera

app = Flask(__name__)

flag = True

# for loading landing page
@app.route('/')
def index():
    return render_template('index.html')

# update video streaming
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera(device_id=DEVICE_ID)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# get the snapshot of current picture
@app.route('/snapshot')
def snapshot():
    save_frame(VideoCamera(device_id=DEVICE_ID))
    path='/tmp/save.png'
    with open(path, 'r') as f:
        response  = make_response(f.read(),200)
    response.headers["Content-Disposition"] = "attachment; filename=%s" % 'snapshot.png'
    return response

def save_frame(camera):
    flag=False
    camera.save_frame()

def gen(camera):
    while flag:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
