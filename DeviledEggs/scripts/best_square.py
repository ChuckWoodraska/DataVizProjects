import os
from PIL import Image

def find_max_square_size(input_directory):
    """
    Determines the largest possible square size that fits within all images in a directory.

    Args:
        input_directory (str): Path to the directory containing images.

    Returns:
        int: The side length of the largest possible square.
    """

    min_dimension = float('1000000')  # Start with a very large value

    for filename in os.listdir(input_directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(input_directory, filename)
            try:
                with Image.open(image_path) as image:
                    width, height = image.size
                    min_dimension = min(min_dimension, width, height)  # Find the smallest dimension
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    return min_dimension

# Example usage
input_directory = '../data/output_images'  # Replace with your image directory
max_square_size = find_max_square_size(input_directory)
print(f"The largest possible square size is: {max_square_size} pixels")
