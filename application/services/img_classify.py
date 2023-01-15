import numpy as np
import cv2
import pyprojroot
from joblib import load

model_folder  =  pyprojroot.here() / "models"

class ImgClassify():
    def __init__(self) -> None:
        self.model = self.load_model()
        self.scaler = self.load_scaler()

    def load_model(self):
        model_path = model_folder / "svm_classifier.joblib"
        svm_model = load(model_path)
        return svm_model
    
    def load_scaler(self):
        scaler_path = model_folder / "scaler.joblib"
        scaler = load(scaler_path)
        return scaler

    def extract_features(self,img) -> list[float]:
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

    def color_classify(self,img)->str:
        features = self.extract_features(img)
        features_np = np.array([features])
        scale_features = self.scaler.transform(features_np)
        prediction = self.model.predict(scale_features)
        return prediction[0]