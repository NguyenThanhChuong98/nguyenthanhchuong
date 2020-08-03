file_name = '1500000 Sales Records.csv'
lines = (line for line in open(file_name))
list_line = (s.rstrip().split(",") for s in lines)
cols = next(list_line)
print(cols)
