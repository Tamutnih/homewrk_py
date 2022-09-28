# 18. Реализовать алгоритм перемешивания списка

import random


def get_list(n, left, right):
    return [random.randint(left, right) for i in range(n)]


def shuffle_list(lst):
    return random.shuffle(lst)


n = 10
left = -20
right = 50

mylist = get_list(n, left, right)
print(mylist)
shuffle_list(mylist)
print(mylist)
