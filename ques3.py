import cv2
import numpy as np
import matplotlib.pyplot as plt


def apply_low_pass_filter(image):
    """Apply a Gaussian Blur (Low-Pass Filter) to smooth the image."""
    return cv2.GaussianBlur(image, (15, 15), 0)


def apply_high_pass_filter(image):
    """Apply a High-Pass Filter by subtracting the low-pass image from the original."""
    low_pass = cv2.GaussianBlur(image, (15, 15), 0)
    high_pass = cv2.subtract(image, low_pass)  # Subtract low frequencies
    return high_pass

def combine_images(img1, img2):
    """Combine two images by resizing them to the same dimensions and adding them together."""
    # Resize img2 to match img1's dimensions
    img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    return cv2.addWeighted(img1, 0.5, img2_resized, 0.5, 0)

def display_images(imgs, titles):
    """Display multiple images in a grid."""
    plt.figure(figsize=(12, 8))
    for i in range(len(imgs)):
        plt.subplot(2, 3, i + 1)
        plt.imshow(cv2.cvtColor(imgs[i], cv2.COLOR_BGR2RGB))
        plt.title(titles[i])
        plt.axis('off')
    plt.tight_layout()
    plt.show()


def main():
    # Step 1: Load two images
    image1 = cv2.imread(r"C:\Users\LENOVO\Downloads\zebra.jpg")  # Replace with your image path
    image2 = cv2.imread(r"C:\Users\LENOVO\Downloads\elephant.jpg")  # Replace with your image path

    # Check if images are loaded correctly
    if image1 is None or image2 is None:
        print("Error: Could not load images.")
        return

    # Step 2: Apply filters
    low_pass_image = apply_low_pass_filter(image1)
    high_pass_image = apply_high_pass_filter(image2)

    # Step 3: Combine images
    combined_image = combine_images(low_pass_image, high_pass_image)
    # Step 4: Display all images
    images = [image1, image2, low_pass_image, high_pass_image, combined_image]
    titles = ["Original Image 1", "Original Image 2",
              "Low-Pass Filtered", "High-Pass Filtered", "Combined Image"]

    display_images(images, titles)


if __name__ == "__main__":
    main()
