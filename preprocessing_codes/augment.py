from PIL import Image, ImageOps
import os
import random

def augment_image(image):
    # Apply random rotation
    angle = random.choice([0, 90, 180, 270])
    image = image.rotate(angle)

    # Randomly apply horizontal flip
    if random.choice([True, False]):
        image = ImageOps.mirror(image)

    # Randomly apply vertical flip
    if random.choice([True, False]):
        image = ImageOps.flip(image)

    return image

# Directory paths
input_dir = "/media/bapary/Office/VGG19/data/Parvez"
output_dir = "/media/bapary/Office/VGG19/data/Parvez"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Number of augmentations per image
num_augmentations = 5

# Loop through each image in the input directory
for image_file in os.listdir(input_dir):
    if image_file.endswith((".png", ".jpg", ".jpeg")):
        image_path = os.path.join(input_dir, image_file)
        image = Image.open(image_path)

        for i in range(num_augmentations):
            augmented_image = augment_image(image)
            output_filename = f"{os.path.splitext(image_file)[0]}_aug_{i+1}.jpg"
            output_path = os.path.join(output_dir, output_filename)
            augmented_image.save(output_path)

        print(f"{num_augmentations} augmented versions of {image_file} saved.")
