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
    if len(int_list) == 0:
        raise ValueError("An empty list was provided")
    try:
        total = 0
        for i in int_list:
            total += i

        return total / len(int_list)
    except TypeError:
        raise TypeError("List contains a non integer value")


def median(int_list):

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
