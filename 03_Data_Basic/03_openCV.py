import cv2
import platform

print('OpenCV version: {}'.format(cv2.__version__))
print('Python version: {}'.format(platform.python_version()))

src = cv2.imread('data3.png')

flipped = cv2.flip(src, -1)

# cv2.imshow('Image', src)
# cv2.imshow('Image flipped', flipped)
# #cv2.imwrite('flipped_penguins.png', flipped) #이미지 저장
# cv2.waitKey(0) # 0 forever
# cv2.destroyAllWindows()

print(src.ndim)
print(src.shape)

#왼쪽 강아지 얼굴만 가져오기
# src_face = src[50:150, 50:150]
# print(src_face.shape)
#
# cv2.imshow('FaceImage', src_face)
# cv2.waitKey(0) # 0 forever
# cv2.destroyAllWindows()


#가운데 강아지 얼굴만 가져오기
# src_face2 = src[80:180, 270:370]
# print(src_face2.shape)
#
# cv2.imshow('FaceImage', src_face2)
# cv2.waitKey(0) # 0 forever
# cv2.destroyAllWindows()

#코끼리 사진 활용
src2 = cv2.imread('elephant2.png')

flipped2 = cv2.flip(src2, -1)

# cv2.imshow('Image', src2)
# cv2.imshow('Image flipped', flipped2)
# #cv2.imwrite('flipped_penguins.png', flipped)
# cv2.waitKey(0) # 0 forever
# cv2.destroyAllWindows()

src_face3 = src2[170:319, 79:205]
src_face4 = src2[70:515, 249:861]
print(src_face3.shape)

cv2.imshow('FaceImage', src_face3)
cv2.imshow('FaceImage2', src_face4)
# cv2.imwrite('Elephant3.png', src_face3) #이미지 저장
# cv2.imwrite('Elephant4.png', src_face4)
cv2.waitKey(0) # 0 forever
cv2.destroyAllWindows()