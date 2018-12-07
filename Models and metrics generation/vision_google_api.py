import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


def get_labels(image_path, auth):
    """
    Returns labels or categories using google vision api
    :param image_path: path
    :param auth: auth using credentials
    :return: Labels list
    """
    # Instantiates client
    client = vision.ImageAnnotatorClient(auth)

    file_name = os.path.join(
        os.path.dirname(image_path))

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Perform label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    return labels



if __name__ == '__main__':
    get_labels("resource.jpg")
