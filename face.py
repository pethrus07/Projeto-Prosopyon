import cv2
import face_recognition as fr

imgIzaias = fr.load_image_file('izaias.jpg')
imgIzaias = cv2.cvtColor(imgIzaias, cv2.COLOR_BGR2RGB)

faceLocalizacao = fr.face_locations(imgIzaias)
cv2.rectangle(imgIzaias(faceLocalizacao[3], faceLocalizacao[0]), (faceLocalizacao[1], faceLocalizacao[2]), (0, 255, 0), 2)
print(faceLocalizacao)
cv2.imshow('imgIzaias', imgIzaias)
cv2.waitKey(0)