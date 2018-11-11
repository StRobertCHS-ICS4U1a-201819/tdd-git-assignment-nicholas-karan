
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

    if len(intList) == 0:
        return -1
    intList.sort()
    lower_half = intList[:len(intList) // 2]


    if len(intList) % 2 == 0:
        value1 = lower_half[len(lower_half) // 2 - 1]
        value2 = lower_half[len(lower_half) // 2]
        return(value1 + value2) / 2
    else:
        return lower_half[len(lower_half) // 2]
