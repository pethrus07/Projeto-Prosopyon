import cv2
from deepface import DeepFace 


imagem= cv2.imread('rostos/iza.jpg')

cap=cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret == False:
        continue

    cv2.imshow('video frame', frame)

    key_pressed = cv2.waitKey(1) & 0xFF

    if key_pressed == ord('q'):
        break

resultado = DeepFace.analyze(imagem, actions=('age', 'gender', 'race'))

print(resultado)

#cap.release()
#cv2.destroyAllWindows