import time
import threading


def count_region_group_1(thread_id,delay):
    list1 = []
    with open(file_name) as file:
        for row in file:
            list1.append(row.split(',')[0])
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
    t1 = threading.Thread(target=count_region_group_1,args=(1,3))
    t2 = threading.Thread(target=count_region_group_1,args=(2,4))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    start_time = time.time()
    print("Time Executed: %s seconds" % (time.time() - start_time))
