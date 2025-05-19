from flask import Flask, render_template, Response
import cv2

cap = cv2.VideoCapture(0)
app = Flask(__name__)


def video():
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        (flag, encodedFrame) = cv2.imencode(".jpg", frame)
        if not flag:
            print('not flag')
            continue
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedFrame) + b'\r\n')


@app.route('/')
def web():
    return render_template('data.html')


@app.route("/video_return")
def video_return():
    return Response(
        video(), mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1234)

cap.release()
