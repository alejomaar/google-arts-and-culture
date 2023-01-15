import numpy as np
import cv2

class Conversion:
    async def read_image(self,file):
        contents = await file.read()
        nparr = np.fromstring(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img

    '''def image_to_bytes(self,img):
        _, buffer = cv2.imencode('.png', img)
        img_bytes = buffer.tobytes()
        return img_bytes'''