import time
import datetime

islocking=False 


def LockingAccount():
    # x = datetime.datetime.now()
 
    # y = x + datetime.timedelta(minutes=10)
    
    # print(x.strftime("%H %M"))
    # print(y.strftime("%H %M"))
    islocking=True


def UnlockingAccount():
    islocking=False

def IsLockAccount():
    print(islocking)
    return islocking

LockingAccount()