# import time
# import sys
# # get the start time
# st = time.time()

# # main program
# # find sum to first 1 million numbers
# sum_x = 0
# for i in range(1000000):
#     sum_x += i

# # wait for 3 seconds
# time.sleep(3)
# print('Sum of first 1 million numbers is:', sum_x)

# # get the end time
# et = time.time()

# # get the execution time
# elapsed_time = et - st
# print('Execution time:', elapsed_time, 'seconds')
# print(sys.getsizeof(sum_x))

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)

from PIL import Image
import math


tpl = ('A', 'C', 'B')
print(tpl)
x = list(tpl)

x[1] = 'B'
x[2] = 'C'
new_tupe = tuple(x)
print('new_tuple', new_tupe)


lst = ['a', 'b', 'c']
print('len of list', len(lst))
lst[1] = 'abc'
print(lst)

print(math.pow(2, 3))
print('square', math.sqrt(225))


# Import required library
# Open Image
# im = Image.open("C:/Users/Anand/Desktop/imgs/background.jpg")
# im.show()
# im.convert('L')
# im.rotate(35).show()
# im.convert('L')


lst = [1, 2, 3, 4, 15, 6]
lst.pop()
print(lst)
