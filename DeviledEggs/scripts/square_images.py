import os
from PIL import Image

def crop_to_square(image_path, output_size):
    """
    Crops an image to a square, preserving the center.

    Args:
        image_path (str): Path to the input image.
        output_size (int): Desired side length of the square output.
    """

    image = Image.open(image_path)
    width, height = image.size

    # Determine the side to crop from
    if width > height:
        left = (width - height) // 2
        right = left + height
        top = 0
        bottom = height
    else:
        left = 0
        right = width
        top = (height - width) // 2
        bottom = top + width

    # Crop the image
    image = image.crop((left, top, right, bottom))

    # Resize to the desired square size
    image = image.resize((output_size, output_size))

    return image

# Parameters
input_directory = '../data/output_images'  # Replace with your image directory
output_directory = '../data/output_squares'  # Replace with the desired output folder
square_size = 768  # Example size

# Create output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Process images
for filename in os.listdir(input_directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # Process common image formats
        image_path = os.path.join(input_directory, filename)
        try:
            cropped_image = crop_to_square(image_path, square_size)
            output_path = os.path.join(output_directory, filename)
            cropped_image.save(output_path)
            print(f"Processed {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

