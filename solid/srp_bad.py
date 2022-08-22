import numpy as np


def math_operations(list_):
    """ Bad example of SRP principle"""
    print(f"the mean is {np.mean(list_)}")
    print(f"the max is {np.max(list_)}")


if __name__ == "__main__":
    math_operations(list_ = [1,2,3,4,5])

