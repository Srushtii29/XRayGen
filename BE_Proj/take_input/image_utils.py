from PIL import Image
from keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np
import cv2
def apply_clahe(image, clip_limit=2.0, tile_grid_size=(8, 8)):
    if len(image.shape) == 3 and image.shape[2] == 3:
        image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    else:
        image_gray = image
    if image_gray.dtype != np.uint8:
        image_gray = cv2.convertScaleAbs(image_gray)
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    image_clahe = clahe.apply(image_gray)
    if len(image.shape) == 3 and image.shape[2] == 3:
        image_clahe = cv2.cvtColor(image_clahe, cv2.COLOR_GRAY2RGB)
    return image_clahe
# def apply_clahe(image, clip_limit=2.0, tile_grid_size=(8, 8)):
#     """
#     Apply Contrast Limited Adaptive Histogram Equalization (CLAHE) to an image.
#     Parameters:
#     image: Input image, can be a file object or a numpy array.
#     clip_limit: Threshold for contrast limiting.
#     tile_grid_size: Size of grid for histogram equalization.
#     Returns:
#     CLAHE-enhanced image as a numpy array.
#     """
#     if isinstance(image, np.ndarray):
#         # Convert numpy array to PIL Image
#         image_pil = Image.fromarray(image)
#     elif isinstance(image, InMemoryUploadedFile):
#         # Read image data from InMemoryUploadedFile
#         image_data = image.read()
#         # Create PIL Image from image data
#         image_pil = Image.open(BytesIO(image_data))
#     else:
#         raise ValueError("Unsupported image type")

#     # Convert image to grayscale if it's in RGB format
#     if image_pil.mode != 'L':
#         image_pil = image_pil.convert('L')

#     # Apply CLAHE
#     clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
#     image_array = np.array(image_pil)
#     image_clahe = clahe.apply(image_array)

#     return image_clahe


# Define the preprocess_image function to resize and preprocess images
def preprocess_image(image):
    image = Image.open(image)
    image = image.resize((224, 224))  # Resize the image to (224, 224)
    image = img_to_array(image)
    image = apply_clahe(image)  # Apply CLAHE preprocessing
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    return image
def classify_fracture(location):
    location_to_type = {
        "thigh_bone": ("long bone", "femur"),
        "shin_bone": ("long bone", "tibia"),
        "calf_bone": ("long bone", "fibula"),
        "upper_arm_bone": ("long bone", "humerus"),
        "forearm_bone": ("long bone", "radius or ulna"),
        "wrist_bone": ("short bone", "carpals"),
        "ankle_bone": ("short bone", "tarsals"),
        "palm_bone": ("short bone", "metacarpals"),
        "foot_bone": ("short bone", "metatarsals"),
        "skull_bone": ("flat bone", "skull"),
        "shoulder_bone": ("flat bone", "scapula"),
        "hip_bone": ("flat bone", "pelvis"),
        "kneecap": ("sesamoid bone", "patella"),
        "spine_bone": ("irregular bone", "vertebrae"),
        "tailbone": ("irregular bone", "coccyx"),
    }
    if location.lower() in location_to_type:
        return location_to_type[location.lower()]
    else:
        return "Unknown"