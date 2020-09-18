import time
from multiprocessing import Process, Lock, Value


def add_500_lock(total, lock):
    for i in range(200):
        time.sleep(0.01)
        lock.acquire()
        total.value += 5
        lock.release()


def sub_500_lock(total, lock):
    for i in range(200):
        time.sleep(0.01)
        lock.acquire()
        total.value -= 5
        lock.release()
if __name__ == '__main__':
    
    total = Value('i', 500)
    lock = Lock()
    add_proc = Process(target=add_500_lock, args=(total, lock))
    sub_proc = Process(target=sub_500_lock, args=(total, lock))

    add_proc.start()
    sub_proc.start()

    add_proc.join()
    sub_proc.join()
    print(total.value)