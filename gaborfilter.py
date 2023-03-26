import numpy
import cv2

img = cv2.imread("img/GS010163_up_1.mp4.jpg", cv2.IMREAD_GRAYSCALE) # pathを間違えるとNoneが返ってきます
# Kanel 45度ずつ
gabor1 = cv2.getGaborKernel((10, 10), 4.0, numpy.radians(0), 9, 0.5, 0)
gabor2 = cv2.getGaborKernel((50, 50), 4.0, numpy.radians(45), 9, 0.5, 0)
gabor3 = cv2.getGaborKernel((10, 10), 4.0, numpy.radians(90), 9, 0.5, 0)
gabor4 = cv2.getGaborKernel((10, 10), 4.0, numpy.radians(135), 9, 0.5, 0)
gabor5 = cv2.getGaborKernel((10, 10), 4.0, numpy.radians(180), 9, 0.5, 0)
gabor6 = cv2.getGaborKernel((10, 10), 4.0, numpy.radians(225), 9, 0.5, 0)
gabor7 = cv2.getGaborKernel((10, 10), 4.0, numpy.radians(270), 9, 0.5, 0)
gabor8 = cv2.getGaborKernel((10, 10), 4.0, numpy.radians(315), 9, 0.5, 0)

# filterを適用
dst1 = cv2.filter2D(img, -1, gabor1)
dst2 = cv2.filter2D(img, -1, gabor2)
dst3 = cv2.filter2D(img, -1, gabor3)
dst4 = cv2.filter2D(img, -1, gabor4)
dst5 = cv2.filter2D(img, -1, gabor5)
dst6 = cv2.filter2D(img, -1, gabor6)
dst7 = cv2.filter2D(img, -1, gabor7)
dst8 = cv2.filter2D(img, -1, gabor8)

# 論理和画像を作成
img_1_2 = cv2.bitwise_or(dst1, dst2)
img_3_4 = cv2.bitwise_or(dst3, dst4)
img_5_6 = cv2.bitwise_or(dst5, dst6)
img_7_8 = cv2.bitwise_or(dst7, dst8)
img_1_2_3_4 = cv2.bitwise_or(img_1_2, img_3_4)
img_5_6_7_8 = cv2.bitwise_or(img_5_6, img_7_8)
img_and = cv2.bitwise_or(img_1_2_3_4, img_5_6_7_8)
# img_1_3 = cv2.bitwise_or(dst1, dst3)
# img_5_7 = cv2.bitwise_or(dst5, dst7)
# img_and = cv2.bitwise_or(img_1_3, img_5_7)

# 画像の表示
# cv2.imshow('gabor', dst2)

# 画像の保存
cv2.imwrite('result/gabor0.jpg',dst1)
cv2.imwrite('result/gabor45.jpg',dst2)
cv2.imwrite('result/gabor90.jpg',dst3)
cv2.imwrite('result/gabor135.jpg',dst4)
cv2.imwrite('result/gabor180.jpg',dst5)
cv2.imwrite('result/gabor225.jpg',dst6)
cv2.imwrite('result/gabor270.jpg',dst7)
cv2.imwrite('result/gabor315.jpg',dst8)

cv2.imwrite('result/gabor_or.jpg',img_and)


# cv2.waitKey()
cv2.destroyAllWindows()

