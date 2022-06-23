import cv2 as cv
import numpy as np

# color를 포함해서 이미지 읽기.
img_basic = cv.imread('dog.jpg', cv.IMREAD_COLOR)
cv.imshow('Image Basic', img_basic)
cv.waitKey(0)
cv.imwrite('result1.png', img_basic)

cv.destroyAllWindows()

# 이미지를 흑백컬러로 읽기.
# 읽어들인 이미지를 cvtColor 함수를 통해 특정한 속성을 가지게 할 수 있음.
img_gray = cv.cvtColor(img_basic, cv.COLOR_BGR2GRAY)
cv.imshow('Image Gray', img_gray)
cv.waitKey(0)
cv.imwrite('result2.png', img_gray)
