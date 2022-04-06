import cv2

cascade_classifier = cv2.CascadeClassifier()
cascade_classifier.load(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")


def file_to_prediction(file: str) -> None:
    image = cv2.imread(file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = cascade_classifier.detectMultiScale(
        gray
    )
    ending = file.split(".")[-1]
    new_file = (
        file.replace("\\images\\", "\\output\\").replace(ending, "").replace(".", "")
        + "_detected"
        + "."
        + ending
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (40, 245, 15), 8)
        cv2.imwrite(new_file, image)
