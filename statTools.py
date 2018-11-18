"""
-----------------------------------------------------------------------
Name:               statTools.py

Purpose: Contains functions for Measures of Central Tendency and Measures
         Includes: mode, range, variance, standard deviation

Author:             Polobotu.K, Gin.N

Created: 08/11/2018
-----------------------------------------------------------------------
"""


import math
def mode(numList):

    """

            Returns the mode of the imputted list
            :param numList: list of values
            :return: mode
    """
    #ensure you have no forms of strings in your list
    for i in range (len(numList)):
        if isinstance(numList[i], str) == True:
            raise TypeError("list contains non integer values")
        else:
            i += 1
            #if all numbers, procceed
    try:
        for i in range(len(numList)):
            if len(numList) <= 1:
                return "no Mode"
            # if there is one or fewer elements, no mode
            else:
                counter_list = []
                for i in range(len(numList)):
                    # loop based on the length of our data array
                    counter_list.append(numList.count(numList[i]))
                    # list of arrays counting frequency of values
                    maxFreq = max(counter_list)
                    if maxFreq <= 1:
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
    """
            Returns the range of a function
            :param numList: list of the numbers
            :return: range
    """
    try:
        #if theres nothing given, empty sequence
        if len(numList) == 0:
            raise ValueError("max () arg is an empty sequence")
        else:

            numList.sort()
            # sort it
            the_range = numList[len(numList) - 1] - numList[0]
            # get the maximum minus the minimum
            return the_range
    except TypeError:
        raise TypeError("list contains non integer values")


def variance(numList):
    """

            Provides the variance from a set of numbers
            :param numList: list of numbers given
            :return: variance
    """
    if len(numList) <= 1:
        # if there are one or fewer terms, no variance
        raise ValueError("no variance if there are one or less values")
    else:
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
    """
            returns the standard deviation(square root) of variance
            :param numList: list of numbers provided
            :return: standard deviation
    """
    if len(numList) <= 1:
        raise ValueError("list contains one or less elements")
    # if there are one or fewer elements, no standard deviation
    try:
        # return square root of variance rounded by 3 digits
        return round(math.sqrt(variance(numList)), 3)
    except TypeError:
        raise TypeError("list contains non integer values")