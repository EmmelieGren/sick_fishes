import cv2
import numpy as np
import random

def rotate_image(image, angle):
    """Rotate the image by a certain angle."""
    height, width = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

# Funktion som var som ett test, när man roterar så försvinner mycket av fisken på bilden eftersom att den inte ändrar storleken på originalet så denna
# gör så att bilden anpassas så att hela originalet är med på bilden, men det blev dock väldigt mycket bakgrund på dessa bilder.
def rotate_and_resize(image, angle):
    height, width = image.shape[:2]

    fill_color=(random.randint(1,255), random.randint(1,255), random.randint(1,255))
    # fill_color = (128, 128, 128)

    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height), borderMode=cv2.BORDER_CONSTANT, borderValue=fill_color)

    cos_theta = abs(rotation_matrix[0, 0])
    sin_theta = abs(rotation_matrix[0, 1])

    new_width = int((width * cos_theta) + (height * sin_theta))
    new_height = int((width * sin_theta) + (height * cos_theta))

    translation_x = (new_width - width) / 2
    translation_y = (new_height - height) / 2
    rotation_matrix[0, 2] += translation_x
    rotation_matrix[1, 2] += translation_y

    rotated_resized_image = cv2.warpAffine(image, rotation_matrix, (new_width, new_height), borderMode=cv2.BORDER_CONSTANT, borderValue=fill_color)

    return rotated_resized_image

def flip_image(image):
    flipped_image = cv2.flip(image, 1)
    return flipped_image

def crop_image(image):
    """Crop the image to 1/4 of the original size."""
    original_height, original_width = image.shape[:2]
    
    quarter_width = original_width // 2
    quarter_height = original_height // 2
    
    start_x = 0 if random.random() < 0.5 else quarter_width
    start_y = 0 if random.random() < 0.5 else quarter_height
    
    cropped_width = original_width // 2
    cropped_height = original_height // 2
    cropped_image = image[start_y:start_y+cropped_height, start_x:start_x+cropped_width]
    
    return cropped_image


def blur_image(image, k_size=5):
    """Blur the image using Gaussian Blur."""
    blurred_image = cv2.GaussianBlur(image, (k_size, k_size), 0)
    return blurred_image

def change_color(image, flag=cv2.COLOR_BGR2GRAY):
    """Change the color of the image."""
    converted_image = cv2.cvtColor(image, flag)
    return converted_image

def adjust_color_balance(image, red_factor=1.0, green_factor=1.0, blue_factor=1.0):
    """Adjust the color balance of the image by modifying red and blue channels."""
    B, G, R = cv2.split(image)

    R = cv2.multiply(R, np.array([red_factor]))
    G = cv2.multiply(G, np.array([green_factor]))
    B = cv2.multiply(B, np.array([blue_factor]))

    return cv2.merge([B, G, R])