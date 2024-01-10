"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40
PREP_TIME_PER_LAYER = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(minutes_cooked):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - minutes_cooked


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the prep time based on layers.

    :param number_of_layers: int - how many layers of pasta.
    :return: int - prep time (in minutes) derived from 'PREP_TIME_PER_LAYER".

    Function that takes the number of layers and works out how lon it will take to prepare using the  `PREP_TIME_PER_LAYER`.
    """
    return number_of_layers * PREP_TIME_PER_LAYER


#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
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