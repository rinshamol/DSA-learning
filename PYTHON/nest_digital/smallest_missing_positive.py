def findSmallestMissingPositive(orderNumbers):
    start = 1
    orderNumbers.sort()
    for num in orderNumbers:
        if num > 0:
            if num == start:
                start += 1
            else:
                return start
orderNumbers = [3, 4, -1, 1]
print(findSmallestMissingPositive(orderNumbers))