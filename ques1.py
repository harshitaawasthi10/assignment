import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
def show(name, n, m, i, Title):
        plt.subplot(n, m, i)
        plt.imshow(name, cmap='gray')
        plt.title(Title)
        plt.axis('off')

image = cv.imread(r'C:\Users\LENOVO\Downloads\car.png', cv.IMREAD_GRAYSCALE)
image2 = cv.imread(r"C:\Users\LENOVO\Downloads\flower.jpg", cv.IMREAD_GRAYSCALE)
plt.figure(figsize=(10, 5))
show(image, 1, 2, 1, "Image 1")
show(image2, 1, 2, 2, "Image 2")
plt.tight_layout()
plt.show()