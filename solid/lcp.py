###
# LCP - “Derived classes must be substitutable for their base classes”
###

import numpy as np
from abc import ABC, abstractmethod


class Operations(ABC):
    """ Operations """
    @abstractmethod
    def operation(self):
        pass


class Mean(Operations):
    """ Mean"""
    def operation( list_):
        print(f"Mean: {np.mean(list_)}")


class Max(Operations):
    """ Max """
    def operation(list_):
        print(f"Max: {np.max(list_)}")


if __name__ == "__main__":
    # Run opertions
    list_= [1,2,3,4,5]
    [operation.operation(list_) for operation in Operations.__subclasses__()]