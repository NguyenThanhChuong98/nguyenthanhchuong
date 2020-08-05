import re
from slugify import slugify


def read_first_N_line(file_name, N):
    with open(file_name) as file:
        for line in(file.readlines()[:N]):
            print(line)


def read_last_N_line(file_name, N):
    with open(file_name) as file:
        for line in (file.readlines()[-N:]):
            print(line)


def search_by_words(file_name, n):
    with open(file_name) as file:
        x = slugify(n)
        print(x)
        for line in (file.readlines()):
            y = slugify(line)
            if x in y:
                print(line)
            else:
                pass


if __name__ == '__main__':
    file_name = "20 records sale.csv"
    N = 5
    n = input("Input your words: ")
    try:
        search_by_words(file_name, n)
    except:
        print('File not found')
