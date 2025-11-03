from skimage.oi import imread, imsave

def read_image(path, as_gray=False):
    image = imread(path, as_gray=as_gray)
    return image
 
def save_image(path, image):
    imsave(path, image)

    