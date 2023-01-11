import cv2
import numpy as np

def extract_features(img) -> list[float]:
    bgr =  img.copy()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

    bgr_mean =  np.mean(bgr,axis=(0,1))
    hsv_mean =  np.mean(hsv,axis=(0,1))
    lab_mean =  np.mean(lab,axis=(0,1))
    bgr_std =  np.std(bgr,axis=(0,1))
    hsv_std =  np.std(hsv,axis=(0,1))
    lab_std =  np.std(lab,axis=(0,1))
    return np.hstack((bgr_mean,hsv_mean,lab_mean,bgr_std,hsv_std,lab_std)).tolist()