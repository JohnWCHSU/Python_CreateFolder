# Pythone v3.6

import os

directory = os.path.dirname("D:\Test\Test\\123.txt")


if not os.path.exists(directory):
    print(directory, "is not existed!!")
    os.makedirs(directory)
else:
    print(directory, "is existed!!")