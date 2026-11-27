import cv2
import matplotlib.pyplot as plt
from diyanLib.imports.cv import cv2_imshow

image = cv2.imread('colorpic.jpg')

image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

cv2_imshow(image_rgb)

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2_imshow(gray_image)

cropped_image = image[100:300,200:400]

cropped_rgb = cv2.cvtColor(cropped_image,cv2.COLOR_BGR2RGB)
cv2_imshow(cropped_rgb)