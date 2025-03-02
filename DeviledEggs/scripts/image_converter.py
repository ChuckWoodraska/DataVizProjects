from PIL import Image
import os
import glob
def convert_jpg_to_png(jpg_file, index):
    """
    Converts a JPG image to a PNG image.

    Args:
        jpg_file (str): Path to the input JPG file.
        png_file (str): Path to the output PNG file.
    """

    image = Image.open(jpg_file)
    output_name = jpg_file.split('_')[1]
    image.save(f'../data/output_images/{output_name}_{index}.png', format='PNG')

# Example usage
# grab all the images in the directory
input_images = glob.glob('../data/images/*.jpg')  # Replace with the path to your JPG files
output_image = 'path/to/output/image.png'  # Replace with the desired output filename

for index, input_image in enumerate(input_images):
    convert_jpg_to_png(input_image, index)
