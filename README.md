# Projeto-Prosopyon
import cv2
from deepface import DeepFace 

## ENGINE DE CAPTURA E PARAMETROS
def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if(len(rostos) > 0):
        return True, rostos
    else:
        return False, []


def get_rostos():
    rostos_conhecidos = []
    nomes_dos_rostos = []


    rosto_cadastrado = reconhece_face(f"images/{name_cad}.png")
    if(rosto_cadastrado[0]):
        rostos_conhecidos.append(rosto_cadastrado[1][0])
        nomes_dos_rostos.append(f"{name_cad}")

    return rostos_conhecidos, nomes_dos_rostos

##SISTEMA DE COMPARAÇÃO DE ROSTOS E RESULTADOS
desconhecido = reconhece_face(f"images/{name_log}_desconhecido.png")
if(desconhecido[0]):
    rosto_desconhecido  = desconhecido[1][0]
    rostos_conhecidos, nomes_dos_rostos = get_rostos()
    resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)
    if resultados == [True]:
        print("="*28)
        console.print(f"{os.linesep}-> Usuário Identificado!", style="green bold")
    elif resultados == [False]:
        console.print(f"{os.linesep}-> Usuário Não Corresponde ao Cadastrado!", style="red bold", )

    for i in range(len(nomes_dos_rostos)):
        resultado = resultados[i]
        if(resultado):
            print("O Rosto de", nomes_dos_rostos[i], "Foi reconhecido.")
            print(f"{os.linesep}")

else:
    print('Não foi encontrado nenhum rosto')

video_capture.release()
cv2.destroyAllWindows()
