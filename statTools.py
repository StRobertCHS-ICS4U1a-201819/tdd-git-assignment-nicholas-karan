import math
def mode(numList):
    try:
        if len(numList) == 1:
            raise ValueError("no mode if there is only one value")
        else:
            counter_list = []
            for i in range(len(numList)):
                # loop based on the length of our data array
                counter_list.append(numList.count(numList[i]))
                # list of arrays counting frequency of values
            maxFreq = max(counter_list)
            if maxFreq == 1:
                # if there are no modes, and the counter counts the mode once, its a failed test
                return "no Mode"
            # found maximum frequency of value, so value appears in list a certain number times
            else:
                maxList = []
                for x in numList:
                    if (numList.count(x) == maxFreq):
                        maxList.append(x)
                        # extract that value
                mode = []
                for x in maxList:
                    if (x not in mode):
                    # remove duplicates
                        mode.append(x)
                return mode
    except TypeError:
        raise TypeError("list contains non integer values")


def func_range(numList):
    try:
        if numList == 0:
            raise ValueError("numList contains zero to one ")
        the_range = max(numList) - min(numList)
        # get the maximum minus the minimum
        return the_range
    except TypeError:
        raise TypeError("list contains non integer values")


def variance(numList):
    if len(numList) <= 1:
        raise ValueError("no variance if there is only one value")
    try:
        mean = sum(numList)/len(numList)
        # get the mean to use later
        dev = []
        #need these for later
        for i in range (len(numList)):
            var = (numList[i] - mean) ** 2
            dev.append(var)
            # shuffle through values and find individual variation
            # find total variation
        avg_var = sum(dev)/len(dev)
        # average of total variation
        return (avg_var)
    #give back final variance

    except TypeError:
        raise TypeError("list contains non integer values")

def stnd_dev(numList):
    try:

        # return square root of variance rounded by 3 digits
        return round(math.sqrt(variance(numList)), 3)
    except TypeError:
        raise TypeError("list contains non integer values")