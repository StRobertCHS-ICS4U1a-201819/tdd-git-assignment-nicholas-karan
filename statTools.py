
#mean, mode, lower quartile, variance
#retun error if non-unique mode

def mean(intList):
    sum = 0
    for i in intList:
        sum += i
    return sum / len(intList)