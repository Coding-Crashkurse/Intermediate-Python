import cv2
import numpy as np

cascade_classifier = cv2.CascadeClassifier()
cascade_classifier.load(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


def bytestring_to_prediction(bytestring: bytes):
    data = np.frombuffer(bytestring, dtype=np.uint8)
    img = cv2.imdecode(data, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascade_classifier.detectMultiScale(gray)
    return faces


def file_to_prediction(file: str):
    image = cv2.imread(file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = cascade_classifier.detectMultiScale(gray)
    return faces
