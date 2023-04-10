import matplotlib.pyplot as plt
import numpy as np
import cv2


image=plt.imread(r'C:\Users\Farvath\OneDrive\Desktop\certificates\google data analytics\superman.jpg')

def img2gray(img):
    gray=np.dot(img[...,0:3],[0.299,0.587,0.144])
    return gray

gray_image=img2gray(image)
plt.imshow(gray_image,cmap="gray")
plt.show()