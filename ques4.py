from PIL import Image, ImageOps
import numpy as np

def is_indonesia_or_poland_flag(image_path):
    
    # Load the image and convert it to RGB for processing
    img = Image.open(image_path).convert('RGB')
    img_gray = ImageOps.grayscale(img)

    # Convert grayscale image to NumPy array and identify edges using basic thresholding
    img_np = np.array(img_gray)
    edges = np.where(img_np > np.percentile(img_np, 80), 255, 0).astype(np.uint8)  # High-intensity edges

    # Mask the original image using detected edges
    mask = edges > 0
    masked_image = np.zeros_like(img_np)
    for i in range(3):  # Apply the mask to each RGB channel
        masked_image[:, :, i] = np.where(mask, np.array(img)[:, :, i], 0)

    # Dynamic detection of the region with the flag
    def compute_average_color(region):
        region_nonzero = region[np.sum(region, axis=2) > 0]  # Ignore black (masked-out) pixels
        if len(region_nonzero) == 0:
            return [0, 0, 0]
        return np.mean(region_nonzero, axis=0)

    # Divide the image into multiple horizontal bands (top, middle, bottom)
    height, width = masked_image.shape[0], masked_image.shape[1]
    
    # Assume the flag occupies significant portions in some bands
    top_band = masked_image[:height//3, :]
    middle_band = masked_image[height//3:2*height//3, :]
    bottom_band = masked_image[2*height//3:, :]

    # Compute average color for each band
    top_avg_color = compute_average_color(top_band)
    middle_avg_color = compute_average_color(middle_band)
    bottom_avg_color = compute_average_color(bottom_band)

    # Logic to identify the flag based on color distribution
    def is_red(color):
        return color[0] > color[1] and color[0] > color[2]

    def is_white(color):
        return color[0] < color[1] and color[0] < color[2] and color[1] > 180 and color[2] > 180

    # Check for Indonesia flag: Red top and white bottom
    if is_red(top_avg_color) and is_white(bottom_avg_color):
        return "The flag is Indonesia."

    # Check for Poland flag: White top and red bottom
    elif is_white(top_avg_color) and is_red(bottom_avg_color):
        return "The flag is Poland."

    return "The image does not match Indonesia or Poland flags."
    
image_path = input("Enter the path of the image: ")
result = is_indonesia_or_poland_flag(image_path)
print(result)
