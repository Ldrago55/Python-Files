from random import *

lower = int(input("Enter lower bound :"))
upper = int(input("Enter upper bound :"))

r = randint(lower, upper)


def guessInit(m, n):
    w = 0
    x = n - m
    while True:
        y = x // 2
        w += 1
        x = y
        if y == 0:
            return w


c = 0

print("\t you have only", guessInit(lower, upper), "chances to guess the number")

while c <= guessInit(lower, upper):
    c += 1
    q = int(input("Enter your guess: "))
    if q < r:
        print("your guess is too low")
    elif q > r:
        print("your guess is too high")
    else:
        print("Congratulations!!!! you did it in", c, "try")
        break
