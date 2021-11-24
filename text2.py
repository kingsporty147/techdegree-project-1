# enter your code below
def pop(list, index):

    if index in list:
        list.pop(index)
        return list
    elif index not in list:
        return "Invalid Index"


pop([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)


# print(1 in [1, 2, 3, 4, 5, 6, 7])
