def sort_total_revenue():
    list1 = []
    with open(file_name) as file:
        for line in file.readlines()[1:]:
            list1.append(line.split(','))
        for i in range(len(list1[-3])):
            j = i - 1
            nxt_element = list1[i]
            while (list1[j] > nxt_element) and (j >= 0):
                list1[j + 1] = list1[j]
                j = j - 1
            list1[j + 1] = nxt_element
        print('\n'.join(map(str, list1)))


def sort_total_cost():
    list1 = []
    with open(file_name) as file:
        for row in file.readlines()[1:]:
            list1.append(row.split(','))
        for i in range(len(list1[-2])):
            j = i - 1
            nxt_element = list1[i]
            while (list1[j] > nxt_element) and (j >= 0):
                list1[j + 1] = list1[j]
                j = j - 1
            list1[j + 1] = nxt_element
        print('\n'.join(map(str, list1)))


def sort_total_profit():
    list1 = []
    with open(file_name) as file:
        for row in file.readlines()[1:]:
            list1.append(row.split(','))
        for i in range(len(list1)[-1]):
            j = i - 1
            nxt_element = list1[i]
            while (list1[j] > nxt_element) and (j >= 0):
                list1[j + 1] = list1[j]
                j = j - 1
            list1[j + 1] = nxt_element
        print('\n'.join(map(str, list1)))


if __name__ == "__main__":
    file_name = "20 records sale.csv"
    sort_total_revenue()
    sort_total_cost()
    sort_total_profit()
