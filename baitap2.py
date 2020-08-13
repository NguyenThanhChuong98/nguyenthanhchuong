import threading
import time


class myThread (threading.Thread):

    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter

    def run(self):
        threadLock.acquire()
        threadLock.release()

threadLock = threading.Lock()


def count_region_group_1():
    list1 = []
    threads = []
    thread1 = myThread("Thread1", 1)
    thread2 = myThread("Thread2", 2)
    thread3 = myThread("Thread3", 3)
    thread4 = myThread("Thread4", 4)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    threads.append(thread1)
    threads.append(thread2)
    threads.append(thread3)
    threads.append(thread4)
    with open(file_name) as file:
        for i in threads:
        	for j in file:
        		list1.append(j.split(',')[0])
        		n = [[x, list1.count(x)] for x in list1]
        print(n)
        file.close()


def count_region_group_2():
    list1 = []
    with open(file_name) as file:
        for row in file:
            list1.append(row.split(',')[0])
        n = [[x, list1.count(x)] for x in list1]
        print(n)
    file.close()


if __name__ == "__main__":
    file_name = "20 records sale.csv"
    start_time = time.time()
    count_region_group_1()
    print("Time Executed: %s seconds" % (time.time() - start_time))
    count_region_group_2()
    print("Time Executed: %s seconds" % (time.time() - start_time))
