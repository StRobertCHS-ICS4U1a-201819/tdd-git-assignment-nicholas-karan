
#mean, median, lower quartile, upper quartile
#retun error if non-unique mode

#refactor this later
def mean(intList):
    if len(intList) == 0:
        raise ValueError("An empty list was provided")
    try:
        total = 0
        for i in intList:
            total += i

        return total / len(intList)
    except TypeError:
        raise TypeError("List contains a non integer value")

def median(intList):
    if len(intList) == 0:
        return -1

    intList.sort()
    middle = len(intList) // 2
    if len(intList) % 2 == 0:
        value1 = intList[middle - 1]
        value2 = intList[middle]
        return (value1 + value2) / 2
    else:
        return intList[middle]

def lQ(intList):

    if len(intList) < 4:
        return -1
    intList.sort()
    lower_half = intList[:len(intList) // 2]


    if len(intList) % 2 == 0:
        value1 = lower_half[len(lower_half) // 2 - 1]
        value2 = lower_half[len(lower_half) // 2]
        return(value1 + value2) / 2
    else:
        return lower_half[len(lower_half) // 2]

def uQ(intList):
    if len(intList) < 4:
        return -1

    intList.sort()
    upper_half = intList[len(intList) // 2:]
    if len(intList) % 2 == 0:
        value1 = upper_half[len(upper_half) // 2 - 1]
        value2 = upper_half[len(upper_half) // 2]
        return(value1 + value2) / 2
    else:
        return upper_half[len(upper_half) // 2]

