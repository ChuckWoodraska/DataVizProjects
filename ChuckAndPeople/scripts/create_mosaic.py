import photomosaic as pm
from skimage.io import imread, imsave

target = '../data/target6.jpg'
image = imread(target)
dims_list = [(25, 25,), (50, 50,), (100, 100,), (125, 125,), (150, 150,), (200, 200,), (250, 250,), (500, 500,)]

# Analyze the collection (the "pool") of images.
pool = pm.make_pool('../data/cap/*.jpg')
for dims in dims_list:
    mos = pm.basic_mosaic(image, pool, dims, depth=1)
    imsave('mosaic_{}x{}_{}.png'.format(dims[0], dims[1], target.split('/')[-1]), mos)
