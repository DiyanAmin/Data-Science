import cv2

image_name = 'color.jpg'

image = cv2.imread('Raw Images\\color.jpg')

gray_image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

resized_image = cv2.resize(gray_image,(224,224))

cv2.imshow('Processed Image',resized_image)

key  = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite(f'p_color.{image_name.split('.')[1]},resized_image)
    print('Image saved.')
else:
    print('Image not saved')

cv2.destroyAllWindows()

print(f"Processed Image Dimensions: {resized_image.shape}")