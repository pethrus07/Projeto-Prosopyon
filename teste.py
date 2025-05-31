import face_recognition as fr
import cv2
import face_recognition_models

imgElon = fr.load_image_file('iza.jpg')

cv2.imshow('Iza',imgElon)
cv2.waitKey(0)