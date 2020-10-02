# Import necessary library
import random
from tabulate import tabulate


# Make a table with 10 rows and 10 columns and specify location of rabbit
Table = []

for vertical in range(10):
    num1 = random.randint(0, 9)  # For stone -> S
    num2 = random.randint(0, 9)  # For carrot -> C
    num3 = random.randint(0, 9)  # For male rabbit -> Rm
    num4 = random.randint(0, 9)  # For female rabbit -> Rf
    res = []

    for horizontal in range(10):
        while (num1 == num2) or (num1 == num3) or (num2 == num3) or (num1 == num4) or (num2 == num4):
            num2 = random.randint(0, 9)
            num3 = random.randint(0, 9)
            num4 = random.randint(0, 9)
        if horizontal == num1:
            res.append("S")
        elif horizontal == num2:
            res.append("C")
        elif (horizontal == num3) and (horizontal == num4):
            res.append("Rb")
        elif vertical in {0, 2, 4, 6, 8}:
            if horizontal == num3:
                res.append("Rm")
            else:
                res.append("-")
        elif vertical in {1, 3, 5, 7, 9}:
            if horizontal == num4:
                res.append("Rf")
            else:
                res.append("-")

    Table.append(res)

# For pigeonhole principle
    if vertical == 9:
        num5 = random.randint(0, 9)
        while (num5 == num1) or (num5 == num2):
            num5 = random.randint(0, 9)
        if (num5 == num3) and (num5 == num4):
            Table[num5][num5] = "Rb"
        elif num5 == num3:
            Table[num5][num5] = "Rm"
        elif num5 == num4:
            Table[num5][num5] = "Rf"
        else:
            Table[num5][num5] = "Rm"

print(tabulate(Table, tablefmt="plain"))
