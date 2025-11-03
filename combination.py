import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms       
from skimage.exposure import structural_similarity


def find_difference(nature1, nature2):
    assert nature1.shape == nature2.shape, "specify 2 images of the same shape"
    gray_image1 = rgb2gray(nature1)
    gray_image2 = rgb2gray(nature2)
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True)
    print("similarity of the images: ", score)
    normalized_difference_image = (difference_image + 1) / 2.0
    return  normalized_difference_image 


def transfer_histogram(nature1, nature2):
    matched_image = match_histograms(nature2, nature1, multichannel=True)
    return matched_image