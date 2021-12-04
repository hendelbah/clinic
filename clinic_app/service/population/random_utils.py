"""
This module provides some utility functions for generating test data
"""
from datetime import date
from random import choices, randint
from string import digits


class RandomNumberGenerator:
    """
    Class for generating unique random numbers as strings with given size.
    Generated numbers are cached to avoid repeats.
    To generate a number call the instance of this class
    """

    def __init__(self, size: int = 9):
        """
        :param size: number of digits of generated numbers
        """
        self.__generated_numbers = set()
        self.__size = size

    def __call__(self) -> str:
        number = ''.join(choices(digits, k=self.__size))
        if number not in self.__generated_numbers:
            self.__generated_numbers.add(number)
            return number
        return self()

    def clear(self):
        """Clear cache"""
        self.__generated_numbers.clear()


random_9d_number = RandomNumberGenerator(9)


def random_date(date_a: date, year_b: date) -> date:
    """
    Generate random date between date_a and date_b (inclusively)

    :param date_a: bottom generation bound
    :param year_b: top generation bound
    """
    ordinal_a = date_a.toordinal()
    ordinal_b = year_b.toordinal()
    ordinal_result = randint(ordinal_a, ordinal_b)
    return date.fromordinal(ordinal_result)