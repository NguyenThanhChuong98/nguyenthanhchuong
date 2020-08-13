def sort_total_revenue():
	sort_list(-3)

def sort_total_cost():
	sort_list(-2)

def sort_total_profit():
	sort_list(-1)

def sort_list(n):
    list1 = []
    with open(file_name) as file:
        for row in file.readlines()[1:]:
            list1.append(row.split(','))
        for i in range(len(list1[n]) - 1):
            for j in range(len(list1[n]) - i - 1):
                if list1[j] > list1[j + 1]:
                    list1[j], list1[j + 1] = list1[j + 1], list1[j]
        print('\n\n'.join(map(str, list1)))

        # for i in range(len(list1[])):
        #     j = i - 1
        #     nxt_element = list1[i]
        #     while (list1[j] > nxt_element) and (j >= 0):
        #         list1[j + 1] = list1[j]
        #         j = j - 1
        #     list1[j + 1] = nxt_element
        # print('\n\n'.join(map(str, list1)))
if __name__ == "__main__":
    file_name = "20 records sale.csv"
    sort_total_revenue()
