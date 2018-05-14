import photomosaic as pm
from skimage.io import imread, imsave
import os
import glob
import shutil
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image


# NOTE: photomosaic doesn't have a way to tell it what tiles its using so I patched it to be able to pass a file path
# to save that data.

# def basic_mosaic(image, pool, grid_dims, *, mask=None, depth=0, matches_fp='./tmp.json'):
#     # Size the image to be evenly divisible by the tiles.
#     image = img_as_float(image)
#     image = rescale_commensurate(image, grid_dims, depth)
#     if mask is not None:
#         mask = rescale_commensurate(mask)
#
#     # Use perceptually uniform colorspace for all analysis.
#     converted_img = perceptual(image)
#
#     # Adapt the color palette of the image to resemble the palette of the pool.
#     adapted_img = adapt_to_pool(converted_img, pool)
#
#     # Partition the image into tiles and characterize each one's color.
#     tiles = partition(adapted_img, grid_dims=grid_dims, mask=mask, depth=depth)
#     tile_colors = [np.mean(adapted_img[tile].reshape(-1, 3), 0)
#                    for tile in tqdm(tiles, desc='analyzing tiles')]
#
#     # Match a pool image to each tile.
#     match = simple_matcher(pool)
#     matches = [match(tc) for tc in tqdm(tile_colors, desc='matching')]
#     with open(matches_fp, 'w') as f:
#         f.write(json.dumps(matches))
#     # Draw the mosaic.
#     canvas = np.ones_like(image)  # white canvas same shape as input image
#     return draw_mosaic(canvas, tiles, matches)


def centroid_histogram(clt):
    # grab the number of different clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()

    # return the histogram
    return hist


def plot_colors(hist, centroids):
    # initialize the bar chart representing the relative frequency
    # of each of the colors
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    # loop over the percentage of each cluster and the color of
    # each cluster
    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar


def dominant_color(target, target_filename):
    # load the image and convert it from BGR to RGB so that
    image = cv2.imread(target)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # reshape the image to be a list of pixels
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    # cluster the pixel intensities
    clt = KMeans(n_clusters=5)
    clt.fit(image)

    # build a histogram of clusters and then create a figure
    # representing the number of pixels labeled to each color
    hist = centroid_histogram(clt)
    bar = plot_colors(hist, clt.cluster_centers_)

    # show our color bart
    fig = plt.figure()
    plt.axis("off")
    plt.imshow(bar)
    fig.savefig('../data/mosaic_dom_color/{}.png'.format(target_filename))


def main_pic_gen():
    target = '../data/main/main.jpg'
    image = imread(target)
    # image_float = img_as_float(image)
    # dims_list = [(25, 25,), (50, 50,), (100, 100,), (125, 125,), (150, 150,), (200, 200,)]
    dims_list = [(150, 150,), ]

    # Analyze the collection (the "pool") of images.
    pool = pm.make_pool('../data/cap_pics/*.jpg')
    target_filename = target.split('/')[-1][:-4]
    for dims in dims_list:
        mos = pm.basic_mosaic(image, pool, dims, depth=1,
                              matches_fp='mosaic_{}x{}_{}.json'.format(dims[0], dims[1], target_filename))
        imsave('mosaic_{}x{}_{}.png'.format(dims[0], dims[1], target_filename), mos)

    # instagram-scraper chuckwoodraska --include-location --media-metadata --comments


def all_pic_gen():
    target_list = os.listdir('../data/cap_pics')
    pool = pm.make_pool('../data/cap_pics/*.jpg')
    for target in target_list:
        target_filename = target.split('/')[-1][:-4]
        dominant_color('../data/cap_pics/{}'.format(target), target_filename)
        mos = pm.basic_mosaic(imread('../data/cap_pics/{}'.format(target)), pool, (100, 100,), depth=1,
                              matches_fp='../data/mosaic_json/{}.json'.format(target_filename))
        imsave('../data/mosaic_pics/{}.png'.format(target_filename), mos)


def progressive_pic_gen():
    for x in range(1, 366):
        shutil.copy('../data/cap_pics/Day{}.jpg'.format(x), '../data/progressive_pool/Day{}.jpg'.format(x))
        pool = pm.make_pool('../data/progressive_pool/*.jpg')
        mos = pm.basic_mosaic(imread('../data/cap_pics/Day{}.jpg'.format(x)), pool, (100, 100,), depth=1,
                              matches_fp='../data/progressive_json/Day{}.json'.format(x))
        imsave('../data/progressive_pics/Day{}.png'.format(x), mos)


def main_pic_thumbnail_gen():
    size = 256, 256
    target = '../data/main/main.jpg'
    im = Image.open(target)
    im.thumbnail(size)
    im.save('../data/main/main.thumbnail', 'PNG')
    target = '../data/main/main.png'
    im = Image.open(target)
    im.thumbnail(size)
    im.save('../data/main/mosaic.thumbnail', 'PNG')

def cap_pics_thumbnail_gen():
    size = 256, 256
    for target in glob.glob('../data/cap_pics/*.jpg'):
        target_filename = target.split('/')[-1][:-4]
        im = Image.open(target)
        im.thumbnail(size)
        im.save('../data/cap_pics_thumbnails/{}.thumbnail'.format(target_filename), 'PNG')


def all_pics_thumbnail_gen():
    size = 256, 256
    for target in glob.glob('../data/mosaic_pics/*.png'):
        target_filename = target.split('/')[-1][:-4]
        im = Image.open(target)
        im.thumbnail(size)
        im.save('../data/mosaic_thumbnails/{}.thumbnail'.format(target_filename), 'PNG')


def progressive_thumbnail_gen():
    size = 256, 256
    for target in glob.glob('../data/progressive_pics/*.png'):
        target_filename = target.split('/')[-1][:-4]
        im = Image.open(target)
        im.thumbnail(size)
        im.save('../data/progressive_thumbnails/{}.thumbnail'.format(target_filename), 'PNG')


main_pic_gen()
all_pic_gen()
progressive_pic_gen()
main_pic_thumbnail_gen()
cap_pics_thumbnail_gen()
all_pics_thumbnail_gen()
progressive_thumbnail_gen()
