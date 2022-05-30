import random
from random import randint

print(random.randint(1, 100))

a=1
while a<=10:
    b=1
    while b<=10:
        c=a*b
        print(c, end=" ")
        b+=1
    print(" ")
    a+=1
