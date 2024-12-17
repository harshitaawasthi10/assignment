import cv2
import numpy as np
import matplotlib.pyplot as plt

def capture_image(camera_index=0):
    cap = cv2.VideoCapture(camera_index)  # Open the webcam
    if not cap.isOpened():
        print("Error: Could not open camera!")
        return None
    ret, frame = cap.read()  # Capture a single frame
    cap.release()  # Release the webcam
    if ret:
        return frame  # Return the captured image
    else:
        print("Error: Could not capture image!")
        return None
#function for grey scaling the image
def grayscale_image(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Function for binary thresholding (black and white)
def threshold_image(image, thresh_value=128):
    _, binary_image = cv2.threshold(image, thresh_value, 255, cv2.THRESH_BINARY)
    return binary_image
def quantize_greyscale(image, levels=16):
    step = 256 // levels
    return (image // step) * step

# Function to apply Sobel filter
def sobel_filter(image):
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combined = cv2.magnitude(sobel_x, sobel_y)
    return np.uint8(sobel_combined)

# Function to apply Canny edge detection
def canny_edge(image, threshold1=50, threshold2=150):
    return cv2.Canny(image, threshold1, threshold2)
# Function to apply Gaussian blur (noise removal)
def gaussian_blur(image, kernel_size=5):
    kernel = (kernel_size, kernel_size)
    return cv2.GaussianBlur(image, kernel, 0)

# Function to sharpen an image
def sharpen_image(image):
    sharpening_kernel = np.array([[0, -1, 0],
                                  [-1, 5, -1],
                                  [0, -1, 0]])
    return cv2.filter2D(image, -1, sharpening_kernel)

# Function to convert RGB to BGR
def rgb_to_bgr(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


def display_results():
    # Capture the image
    image = capture_image(0)
    if image is None:
        return

    # Process the image
    grey_image = grayscale_image(image)
    binary_image = threshold_image(grey_image)
    quantized_image = quantize_greyscale(grey_image, 16)
    sobel_image = sobel_filter(grey_image)
    canny_image = canny_edge(grey_image)
    blurred_image = gaussian_blur(grey_image)
    sharpened_image = sharpen_image(blurred_image)
    bgr_image = rgb_to_bgr(image)

    # Plot the images in a 2x4 grid
    plt.figure(figsize=(12, 6))

    plt.subplot(2, 4, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(2, 4, 2)
    plt.imshow(grey_image, cmap='gray')
    plt.title("Greyscale")
    plt.axis('off')

    plt.subplot(2, 4, 3)
    plt.imshow(binary_image, cmap='gray')
    plt.title("Thresholding")
    plt.axis('off')

    plt.subplot(2, 4, 4)
    plt.imshow(quantized_image, cmap='gray')
    plt.title("16 Grey Colors")
    plt.axis('off')

    plt.subplot(2, 4, 5)
    plt.imshow(sobel_image, cmap='gray')
    plt.title("Sobel Filter")
    plt.axis('off')

    plt.subplot(2, 4, 6)
    plt.imshow(canny_image, cmap='gray')
    plt.title("Canny Edge Detection")
    plt.axis('off')

    plt.subplot(2, 4, 7)
    plt.imshow(blurred_image, cmap='gray')
    plt.title("Gaussian Blur")
    plt.axis('off')

    plt.subplot(2, 4, 8)
    plt.imshow(sharpened_image, cmap='gray')
    plt.title("Sharpened Image")
    plt.axis('off')

    plt.tight_layout()
    plt.show()

    # BGR color check
    print("BGR Conversion Done! Default IDE Theme: Likely Dark/Light depending on IDE settings.")


# Run the main function
if __name__ == "__main__":
    display_results()