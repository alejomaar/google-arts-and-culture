from matplotlib import pyplot as plt
import cv2


def imgshow(img) -> None:
    '''
    Plot image in RGB Color Space
    '''
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.show()