from PIL import Image
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog

def is_indonesia_or_poland_flag(image_path):
    try:
        # Open the image and convert it to RGB
        img = Image.open(image_path).convert('RGB')
        img_array = np.array(img)

        # Get the height and width of the image
        height, width, _ = img_array.shape

        # Check if the image has a valid aspect ratio (i.e., two horizontal bands)
        if height < 2 or width < 2:
            return "Invalid image size"

        # Divide the image into two halves (upper and lower)
        upper_half = img_array[:height//2, :, :]
        lower_half = img_array[height//2:, :, :]

        # Check if the upper half is predominantly red and the lower half is predominantly white
        upper_red = np.all(upper_half[:, :, 0] > upper_half[:, :, 1]) and np.all(upper_half[:, :, 0] > upper_half[:, :, 2])
        lower_white = np.all(lower_half[:, :, 0] > lower_half[:, :, 1]) and np.all(lower_half[:, :, 1] > lower_half[:, :, 2])

        # If the upper half is red and the lower half is white, it's Indonesia
        if upper_red and lower_white:
            return "This is the flag of Indonesia"

        # Check if the upper half is predominantly white and the lower half is red (Poland flag)
        upper_white = np.all(upper_half[:, :, 0] > upper_half[:, :, 1]) and np.all(upper_half[:, :, 1] > upper_half[:, :, 2])
        lower_red = np.all(lower_half[:, :, 0] > lower_half[:, :, 1]) and np.all(lower_half[:, :, 0] > lower_half[:, :, 2])

        # If the upper half is white and the lower half is red, it's Poland
        if upper_white and lower_red:
            return "This is the flag of Poland"

        return "The image doesn't match either the Indonesia or Poland flag"

    except Exception as e:
        return f"Error: {str(e)}"


# Use tkinter to open a file dialog for image selection
root = tk.Tk()
root.withdraw()  # Hide the main window

# Let the user select the image file
image_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])

if image_path:
    if not os.path.exists(image_path):
        print(f"File not found at {image_path}")
    else:
        result = is_indonesia_or_poland_flag(image_path)
        print(result)
else:
    print("No file selected.")