import time

def debug(log, filename, flag=1) :
    if flag == 1 :
        print(filename)
        print(time.strftime('%c', time.localtime(time.time())), __name__, log)