import cv2
import time
import os
import sqlite3
import dlib
import glob
import numpy as np
from skimage import io
from scipy.spatial import distance
import win32com.client as wincl
import config
import datetime
con=config.con

#загружаем сверточные нейросети с официального сайта dlib
sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
#сверточная нейросеть выделения на фотографии лица с помощью 68 ключевых точек
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
#сверточная нейросеть выделяющая дискриптор из лиц
detector = dlib.get_frontal_face_detector()

ready_to_detect_identity = True

windows10_voice_interface = wincl.Dispatch("SAPI.SpVoice")


def webcam_face_recognizer():
    global ready_to_detect_identity
    finishTime = datetime.datetime.now() + datetime.timedelta(seconds=15)

    #cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)
    
    while vc.isOpened():
        #включение вебкамеры
        _, frame = vc.read()
        img = frame


        if ready_to_detect_identity:
            cur=con.cursor()
            cur.execute(f"SELECT * FROM users;")


            # находим лицо с помощью вебкамеры
            dets = detector(img, 1)
            for k, d in enumerate(dets):
                shape = sp(img, d)
            # извлекаем дискриптор из лица
            global face_descriptor1
            #исключение, чтобы программа не крашелась когда сразу не смогла распознать лицо
            try:
                face_descriptor1 = facerec.compute_face_descriptor(img, shape)
            except:
                continue
            global mm
            mm = False

            # цикл по БД
            while True:

                if datetime.datetime.now()>= finishTime:
                    print("хуй")
                    return False
                global one_result
                one_result = cur.fetchone()
                if one_result == None:
                    break
                # преобразование строки в массив
                line = []
                line = one_result[7]
                face_descriptor2 = np.asfarray(line, float)
                #face_descriptor2 = float(one_result[7])
                # высчитывание евклидово расстояние
                a = distance.euclidean(face_descriptor1, face_descriptor2)
                # цикл отбора нужных людей
                while a < 0.521:
                    print(one_result[1])
                    cv2.imwrite('example.png', img)
                    welcome_users(one_result[1])
                    return True
                #welcome_users(one_result[1])

        key = cv2.waitKey(100)
        #cv2.imshow("preview", img)

        if key == 27:  # exit on ESC
            break
    #cv2.destroyWindow("preview")
#аудиозапись о успешном прохождение авторизации по лицу
def welcome_users(identities):
    global ready_to_detect_identity
    welcome_message = 'доброго тебе времени суток %s' % identities
    windows10_voice_interface.Speak(welcome_message)
    ready_to_detect_identity = True

'''if __name__ == '__main__':
    webcam_face_recognizer()'''



