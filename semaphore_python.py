from threading import Semaphore, Thread
import time

sem_obj = Semaphore(2)

def func_lazy(n):
    sem_obj.acquire()
    time.sleep(int(n))
    string_out = f" Sleep completed with time {str(n)}"
    print(string_out)
    sem_obj.release()
    return string_out

t1 = Thread(target=func_lazy, args=("10",), daemon=False)
t2 = Thread(target=func_lazy, args=('2'), daemon= True)
t3 = Thread(target= func_lazy, args=('3'), daemon= True)
t4 = Thread(target=func_lazy, args=('4'))

print("main thread")

t1.start()
t2.start()
t3.start()
t4.start()