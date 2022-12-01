import datetime

dt_now = datetime.datetime.now()

def debug(log, filename, flag=1) :
    if flag == 1 :
        print(dt_now.strftime('%Y.%m.%d %H:%M:%S'), filename, log)