from montages import build_montages
from datetime import datetime
import numpy as np
import imagezmq
import cv2

imageHub = imagezmq.ImageHub()
frameDict = {}
lastActive = {}
lastActiveCheck = datetime.now()
ACTIVE_CHECK_SECONDS = 10
width = 400
w, h = (width, int(480 * width / float(640)))

while True:
    (rpiName, frame) = imageHub.recv_image()
    imageHub.send_reply(b'OK')

    if rpiName not in lastActive.keys():
        print(f"[INFO] receiving data from {rpiName}...")

    lastActive[rpiName] = datetime.now()

    blob = cv2.dnn.blobFromImage(
        cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)

    cv2.putText(
        frame, rpiName, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    frameDict[rpiName] = frame
    montages = build_montages(frameDict.values(), (w, h), (2, 2))
    for (i, montage) in enumerate(montages):
        cv2.imshow(f"server monitor ({i})", montage)

    if (datetime.now() - lastActiveCheck).seconds > ACTIVE_CHECK_SECONDS:
        for (rpiName, ts) in list(lastActive.items()):
            if (datetime.now() - ts).seconds > ACTIVE_CHECK_SECONDS:
                print(f"[INFO] lost connection to {rpiName}...")
                lastActive.pop(rpiName)
                frameDict.pop(rpiName)

        lastActiveCheck = datetime.now()

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()
