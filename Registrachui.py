import dlib
from skimage import io

def import_photo_bd(path, login):
    try:
        print(path)
        #загружаем сверточные нейросети с официального сайта dlib
        sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
        #сверточная нейросеть выделения на фотографии лица с помощью 68 ключевых точек
        facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
        #сверточная нейросеть выделяющая дискриптор из лиц
        detector = dlib.get_frontal_face_detector()

        img = io.imread(path)#Проложить путь до файла
        dets = detector(img, 1)
        for k, d in enumerate(dets):
            shape = sp(img, d)
        face_descriptor1 = facerec.compute_face_descriptor(img, shape)
        print(face_descriptor1)#Загрузить дескриптор в БД

        #Загрузка дескриптора в бд
        #cur.execute(f"UPDATE users SET face=\'{face_descriptor1}\' WHERE login=\'{login}\';")
        #Удалить файл
        return True
    except:
        return False