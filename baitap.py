def read_file():
    file_name = "20 records sale.csv"
    n = open(file_name, "r")
    for lines in n:
        print(lines)
    n.close()

if __name__ == "__main__":
    read_file()
