# print 1 3 5 7 9 from given list

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i, item in enumerate(l): # i is index and item is the element of list
    if(item % 2 != 0):
        print(item)


