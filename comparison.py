import numpy as np
from PIL import Image
from sklearn.metrics.pairwise import euclidean_distances
import os


def image_comparison(my_image, image_objects):
    """
    This function is to rank all images according to euclidean function

    :param image_objects: the photos from the photographer
    :param my_image: image to be compared
    :return :return a list of tuple structure
    (photo_name,euclidean_difference,photographer_id)
    """
    # open my image
    my_image = Image.open(my_image)
    # resize the image
    my_image = my_image.resize((400, 400))
    # convert the image to ndarray
    my_image = np.array(my_image)
    # flatten the image
    my_image = my_image.flatten()

    # create a list for compared images
    compared_images = []

    for image_object in image_objects:
        image = Image.open(os.path.join(os.getcwd(), "static/" + image_object["photo"]))
        # resize the image
        image = image.resize((400, 400))
        # turn image into numpy nd array
        image = np.array(image)
        # flatten the image
        image = image.flatten()
        # get the euclidean distance
        difference = euclidean_distances([image], [my_image])
        # add a tuple of the photo id and the euclidean difference
        compared_images.append(
            (image_object["photo"], difference[0][0], image["photographid"])
        )
    # return sorted  according to the euclidean difference
    return sorted(compared_images, key=lambda x: x[1])
