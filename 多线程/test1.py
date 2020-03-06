import threading
import time


def get_thread_a():
    print("get thread A started")
    time.sleep(3)
    print("get thread A end")


def get_thread_b():
    print("get thread B started")
    time.sleep(5)
    print("get thread B end")


if __name__ == "__main__":
    thread_a = threading.Thread(target=get_thread_a)
    thread_b = threading.Thread(target=get_thread_b)
    start_time = time.time()
    thread_b.setDaemon(True)
    thread_a.start()
    thread_b.start()
    thread_a.join()

    end_time = time.time()
    print("execution time: {}".format(end_time - start_time))