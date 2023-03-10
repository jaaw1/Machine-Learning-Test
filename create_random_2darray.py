# File name: create_random_2darray.py
# Author: Jaani Nurisalo
# Description: Creates random 2d array (asks user for size)
# Date: 3.2.2023


from numpy import random


def create_2d_array(size=0):
    if size == 0:
        ar_size = int(input("Size of data set: "))
    else:
        ar_size = size
    return random.random((ar_size, ar_size))


if __name__ == '__main__':

    print(create_2d_array())


