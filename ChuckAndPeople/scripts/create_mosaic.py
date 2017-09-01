from skimage import data
import matplotlib.pyplot as plt
from skimage.io import imread
image = imread('../data/target5.jpg')
# image = data.chelsea()

import photomosaic as pm

# Generate a collection of solid-color square images.
# pm.rainbow_of_squares('pool/')

# Analyze the collection (the "pool") of images.
pool = pm.make_pool('../data/pics/*.jpg')
mos = pm.basic_mosaic(image, pool, (200, 200), depth=3)

from skimage.io import imsave
imsave('mosaic.png', mos)