def mode(numList):
    try:
        if len(numList) == 1:
            return numList
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
    except:
        return -1

def func_range(numList):
    try:
        the_range = max(numList) - min(numList)
        # get the maximum minus the minimum
        return the_range
    except:
        return -1