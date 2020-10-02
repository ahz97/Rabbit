# Import necessary library
import random
from tabulate import tabulate


class RandNum:
    num = None

    def rand_gen(self):
        self.num = random.randint(0, 9)
        return self.num


class Stone:
    s = None

    def stone_gen(self):
        self.s = "S"
        return self.s


class Carrot:
    c = None

    def carrot_gen(self):
        self.c = "C"
        return self.c


class RabbitMale:
    rm = None

    def rabbit_male_gen(self):
        self.rm = "Rm"
        return self.rm


class RabbitFemale:
    rf = None

    def rabbit_female_gen(self):
        self.rf = "Rf"
        return self.rf


class RabbitBaby:
    rb = None

    def rabbit_baby_gen(self):
        self.rb = "Rb"
        return self.rb


# Make a table with 10 rows and 10 columns and specify location of rabbit
Table = []

for vertical in range(10):
    num1_1 = RandNum()  # For stone -> S
    num1 = num1_1.rand_gen()
    num2_2 = RandNum()  # For carrot -> C
    num2 = num2_2.rand_gen()
    num3_3 = RandNum()  # For male rabbit -> Rm
    num3 = num3_3.rand_gen()
    num4_4 = RandNum()  # For female rabbit -> Rf
    num4 = num4_4.rand_gen()
    res = []

    for horizontal in range(10):
        while (num1 == num2) or (num1 == num3) or (num2 == num3) or (num1 == num4) or (num2 == num4):
            num2 = num2_2.rand_gen()
            num3 = num3_3.rand_gen()
            num4 = num4_4.rand_gen()
        if horizontal == num1:
            res_n = Stone()
            res.append(res_n.stone_gen())
        elif horizontal == num2:
            res_n = Carrot()
            res.append(res_n.carrot_gen())
        elif (horizontal == num3) and (horizontal == num4):
            res_n = RabbitBaby()
            res.append(res_n.rabbit_baby_gen())
        elif vertical in {0, 2, 4, 6, 8}:
            if horizontal == num3:
                res_n = RabbitMale()
                res.append(res_n.rabbit_male_gen())
            else:
                res.append("-")
        elif vertical in {1, 3, 5, 7, 9}:
            if horizontal == num4:
                res_n = RabbitFemale()
                res.append(res_n.rabbit_female_gen())
            else:
                res.append("-")

    Table.append(res)

# For pigeonhole principle
    if vertical == 9:
        num5_5 = RandNum()
        num5 = num5_5.rand_gen()
        while (num5 == num1) or (num5 == num2):
            num5 = num5_5.rand_gen()
        if (num5 == num3) and (num5 == num4):
            res_n = RabbitBaby()
            Table[num5][num5] = res_n.rabbit_baby_gen()
        elif num5 == num3:
            res_n = RabbitMale()
            Table[num5][num5] = res_n.rabbit_male_gen()
        elif num5 == num4:
            res_n = RabbitFemale()
            Table[num5][num5] = res_n.rabbit_female_gen()
        else:
            res_n = RabbitMale()
            Table[num5][num5] = res_n.rabbit_male_gen()

print(tabulate(Table, tablefmt="plain"))
