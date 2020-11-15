import dlib
from skimage import io
import config
con=config.con


def import_photo_bd(path, login):
    try:
        #print(path)
        #загружаем сверточные нейросети с официального сайта dlib
        sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
        #сверточная нейросеть выделения на фотографии лица с помощью 68 ключевых точек
        facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
        #сверточная нейросеть выделяющая дискриптор из лиц
        detector = dlib.get_frontal_face_detector()
        #cur = con.cursor()

        img = io.imread(path)#Проложить путь до файла
        dets = detector(img, 1)
        for k, d in enumerate(dets):
            shape = sp(img, d)
        face_descriptor1 = facerec.compute_face_descriptor(img, shape)
        #print(type(face_descriptor1))#Загрузить дескриптор в БД
        descriptorDB = ""
        for i in range(len(face_descriptor1)):
            if i == len(face_descriptor1)-1:
                descriptorDB += f"{face_descriptor1[i]}"
            else:
                descriptorDB += f"{face_descriptor1[i]}, "
        #print(descriptorDB)

        #face_descriptor1.appand()
        #Загрузка дескриптора в бд
        #cur.execute("UPDATE users SET face='{"+f"{face_descriptor1}"+"}'"+f" WHERE login='{login}';")
        #cur.close()
        #Удалить файл
        return descriptorDB
    except:
        return descriptorDB