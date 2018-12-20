'''
Python程序调试的小工具集合

'''


from time import time
from os import system
system('')

def Timer():
    '''
    计时器，用于统计一段代码运行的时间
    '''
    _time_stamp=time()

    def _timer(flag="",reset=False):
        nonlocal _time_stamp
        if reset:
            _time_stamp=time()
        else:

            outputstr="\033[1;31;40m[timer]\033[0m"+"\033[1;33;40m <%s> \033[0m"+":\033[1;32;40m %.3f \033[0m"

            print(outputstr%(flag,time()-_time_stamp))
            _time_stamp=time()

    return _timer

TIMER=Timer()

if __name__ == "__main__":
    print(123321)
    from time import sleep
    TIMER(__doc__)
    TIMER("123")
    for i in range(3):
        sleep(i)
        TIMER("sleep "+str(i)+" s")