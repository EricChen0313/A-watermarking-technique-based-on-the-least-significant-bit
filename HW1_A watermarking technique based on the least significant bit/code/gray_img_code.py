import cv2


image = cv2.imread('resized_effect.jpg')
output_ROTATE_180 = cv2.rotate(image, cv2.ROTATE_180)
image = cv2.cvtColor(output_ROTATE_180, cv2.COLOR_BGR2GRAY)

cv2.imshow('Result_effect', image)
cv2.imwrite('resized_gray_effect.jpg', image)
cv2.waitKey(0)

