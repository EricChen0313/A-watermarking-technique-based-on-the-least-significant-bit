import cv2
import numpy as np

# 讀取圖像
main = cv2.imread("resized_gray_main.jpg", cv2.IMREAD_GRAYSCALE) #main
effect = cv2.imread("resized_gray_effect.jpg", cv2.IMREAD_GRAYSCALE) #effect
cv2.imshow("main", main)
  
# print(main[719, 404]) #確認是否有添加浮水印
# print('----------------------------------------------------')

# 加入浮水印
for i in range(effect.shape[0]):
    for j in range(effect.shape[1]):
        main[i, j] = (main[i, j] & 0xFC) + ((effect[i, j] & 0xC0) >> 6) 
        #原圖只取前6個bit，將浮水印的前2個bit加入原圖的後2個bit

# print(main[719, 404]) #確認是否有添加浮水印

# 寫入結果圖像
cv2.imwrite("new_main.png", main)

# 讀取結果圖像
output = cv2.imread("new_main.png", cv2.IMREAD_GRAYSCALE)

#輸出所嵌入的浮水印圖像
for i in range(effect.shape[0]):
    for j in range(effect.shape[1]):
        main[i, j] = (output[i, j] << 6) 
        #將結果圖像往左6個bit，即可將加入的浮水印輸出

# print(main[719, 404]) #確認是否有添加浮水印

# 寫入結果圖像
cv2.imwrite("result of effect.png", main)
#------------------------------------------------------------------

# 顯示圖像
cv2.imshow("effect", effect)
cv2.imshow("result", output)
cv2.imshow("output of effect", main)
cv2.waitKey(0)
cv2.destroyAllWindows()