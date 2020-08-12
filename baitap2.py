import time


def count_region_group_1():
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
    start_time = time.time()
    count_region_group_1()
    print("Time Executed: %s seconds" % (time.time() - start_time))
