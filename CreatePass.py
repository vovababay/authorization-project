import random
#Генерация кода для каждого пользователя
def CreatePassword(count):
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password =''
    for _ in range(count):
        password += random.choice(chars)
    return password










   