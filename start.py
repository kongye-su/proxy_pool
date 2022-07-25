import os
import threading

def func(cmd):
    os.system(cmd)
thread1 = threading.Thread(target=func,args=("redis-server",))
thread2 = threading.Thread(target=func,args=("f: & cd F:\Code\python\python-proxy\proxy_pool & conda activate proxy & python proxyPool.py schedule",))
thread3 = threading.Thread(target=func,args=("f: & cd F:\Code\python\python-proxy\proxy_pool & conda activate proxy & python proxyPool.py server",))

thread2.start()
thread1.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()