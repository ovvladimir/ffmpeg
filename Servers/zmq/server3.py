import cv2
import imagezmq

image_hub = imagezmq.ImageHub()

while True:
    name, image = image_hub.recv_image()
    image_hub.send_reply(b'OK')
    cv2.imshow(name, image)
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
