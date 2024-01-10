"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(minutes_cooked):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - minutes_cooked

def preparation_time_in_minutes(number_of_layers):
    """Calculate the prep time based on layers.

    :param number_of_layers: int - how many layers of pasta.
    :return: int - prep time (in minutes) derived from 'PREPARATION_TIME".

    Function that takes the number of layers and works out how lon it will take to prepare using the  `PREPARATION_TIME`.
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time.

    :param number_of_layers: int - how many layers of pasta.
    :param elapsed_bake_time: int - baking time already elapsed.

    :return: int - total elapsed time (in minutes) derived from 'elapsed_bake_time' and the 'preparation_time_in_minutes' function.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and how many layers and returns how many minutes the lasagna has taken to prepare
    based on the `elapsed_bake_time` and 'number_of_layers'.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time