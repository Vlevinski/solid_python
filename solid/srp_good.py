import numpy as np


def get_mean(list_):
    """ Mean of the list of numbers """
    print(f"Mean: {np.mean(list_)}")


def get_max(list_):
    """ Max of the list of numbers """
    print(f"Max: {np.max(list_)}")


if __name__ == "__main__":
    get_mean([1, 2, 3, 4, 5])
    get_max([1, 2, 3, 4, 5])
