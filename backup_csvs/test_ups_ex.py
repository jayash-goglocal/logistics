file = open("final.csv", "r")



for line in file:
    print(len(line.split(",")))