def simple_search(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            return i
    return None

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5

simple_search(arr, target)