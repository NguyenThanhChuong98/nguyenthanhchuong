def sort_total_revenue():
    list1 = []
    with open(file_name) as file:
        for row in file:
            list1.append(row.split(',')[-3])
        list1.sort()
        print(list1)


def sort_total_cost():
	list1 = []
	with open(file_name) as file:
		for row in file:
			list1.append(row.split(',')[-2])
		list1.sort()
		print(list1)


def sort_total_profit():
	list1 = []
	with open(file_name) as file:
		for row in file:
			list1.append(row.split(',')[-1])
		list1.sort()
		print(list1)

if __name__ == "__main__":
    file_name = "20 records sale.csv"
    sort_total_revenue()
    sort_total_cost()
    sort_total_profit()
