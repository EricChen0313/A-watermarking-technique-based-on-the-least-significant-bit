import cv2
img = cv2.imread('effect.jpg') #('main.jpg')
output_1 = cv2.resize(img, (405, 720))   # 產生 405x720 的圖
cv2.imwrite('resized_effect.jpg', output_1)
