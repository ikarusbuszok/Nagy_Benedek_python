import random


def elagazas():
    print(random.randint(1, 50))
    szam = 0
    if szam % 5 == 0:
        print(f"I/A\n\tA szám 5-tel osztható")
    elif szam % 3 == 0:
        print(f"I/B\n\tA szám 3-mal osztható")
    elif szam % 3 % 5 == 0:
        print(f"I/C\n\tA szám 3-mal és 5-tel is osztható")
