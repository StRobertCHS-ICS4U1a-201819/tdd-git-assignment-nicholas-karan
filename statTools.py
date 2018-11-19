"""
-------------------------------------------------------------------------------
Name:		statTools.py

Purpose:    Contains functions for Measures of Central Tendency and Measures of Spread
            Includes: mean, median, lower quartile, upper quartile

Author:		Gin.N, Polobotu.K

Created:    08/11/2018
------------------------------------------------------------------------------
"""


def mean(int_list):
    """
            Returns the mean of the inputted list
            :param int_list: list of values
            :return: mean
            Author: Gin.N
    """
    # Check if length of the list is 0
    if len(int_list) == 0:
        raise ValueError("An empty list was provided")

    # Check if the list contains a non integer value
    try:

        # Find the mean
        return sum(int_list) / len(int_list)
    except TypeError:
        raise TypeError("List contains a non integer value")


def median(int_list):
    """
           Returns the median of the inputted list
           :param int_list: list of values
           :return: median
           Author: Gin.N
    """
    # Check to see if the list contains any non-integer values
    try:
        # Sort the list
        int_list.sort()

        # Check if the list is empty
        if len(int_list) == 0:
            raise ValueError("An empty list was provided")

        # Check if the list has an even or odd length to determine the median
        elif len(int_list) % 2 == 0:
            return (int_list[(len(int_list) // 2) - 1] + int_list[len(int_list) // 2]) / 2
        else:
            return int_list[len(int_list) // 2]

    except TypeError:
        raise TypeError("List contains a non integer value")


def lower_quartile(int_list):
    """
           Returns the lower quartile of the inputted list
           :param int_list: list of values
           :return: int, lower quartile
           Author: Gin.N
    """

    # Check to see if the list contains any non-integer values
    try:
        # Check if the length is less than 4, returns -1 because its not possible
        if len(int_list) < 4:
            return -1

        # Sort the list
        int_list.sort()

        # Find the values of the list until the median, lower half of the list
        lower_half = int_list[:len(int_list) // 2]

        # Finds median of the lower half of the list
        if len(int_list) % 2 == 0:
            value1 = lower_half[len(lower_half) // 2 - 1]
            value2 = lower_half[len(lower_half) // 2]
            return(value1 + value2) / 2
        else:
            return lower_half[len(lower_half) // 2]
    except TypeError:
        raise TypeError("List contains a non integer value")


def upper_quartile(int_list):
    """
           Returns the upper quartile of the inputted list
           :param int_list: list of values
           :return: int, upper quartile
           Author: Gin.N
    """

    # Check to see if the list contains any non-integer values
    try:
        # Check if the length is less than 4, returns -1 because its not possible
        if len(int_list) < 4:
            return -1

        # Sort the list
        int_list.sort()

        # Find the values of the list from the median to the end, upper half of the list
        upper_half = int_list[len(int_list) // 2:]

        # Finds median of the lower half of the list
        if len(int_list) % 2 == 0:
            value1 = upper_half[len(upper_half) // 2 - 1]
            value2 = upper_half[len(upper_half) // 2]
            return(value1 + value2) / 2
        else:
            return upper_half[len(upper_half) // 2]
    except TypeError:
        raise TypeError("List contains a non integer value")

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
            Returns the range of a function, maximum minus minimum
            :param numList: list of numbers that we draw our data from
            :return: range
    """

    if len(numList) == 0:
        # if there is no values, no range, raise an error
        raise ValueError ("no values given")
    else:

        try:
            #get the range
            return (max(numList) - min(numList))

        except TypeError:
            #raise an error if we are given a string
            raise TypeError("cannot take in strings")



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
