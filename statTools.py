
#mean, mode, lower quartile, upper quartile
#retun error if non-unique mode

#refactor this later
def mean(intList):
    sum = 0
    if len(intList) == 0:
        return 0
    else:
        for i in intList:
            sum += i

        return sum / len(intList)

#refactor
def mode(intlist):
    return 5

def lQ(intList):
    return 3
