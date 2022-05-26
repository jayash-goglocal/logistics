file = open("aramex.csv", "r")


for line in file:
    print(len(line.split(",")))