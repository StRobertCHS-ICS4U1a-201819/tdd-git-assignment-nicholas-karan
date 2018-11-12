def mode(numList):
    counter_list = []
    for i in range(len(numList)):
        # loop based on the length of our data array
        counter_list.append(numList.count(numList[i]))
        # list of arrays counting frequency of values
    maxFreq = max(counter_list)
    return maxFreq
    # found maximum frequency of value, so value appears 3 times