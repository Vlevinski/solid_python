import numpy as np
from abc import ABC, abstractmethod


class Operations(ABC):
    """Operations"""

    @abstractmethod
    def operation(self):
        pass


class Mean(Operations):
    """Compute Max"""
    def __init__(self):
        pass

    def operation( list_):
        print(f"The mean is {np.mean(list_)}")


class Max(Operations):
    """Compute Max"""

    def operation(list_):
        print(f"The max is {np.max(list_)}")


class Main:
    """Main"""

    @abstractmethod
    def get_operations(list_):
        # __subclasses__ will return all classes inheriting from Operations
        for operation in Operations.__subclasses__():
            operation.operation(list_)


if __name__ == "__main__":
    Main.get_operations(list_=[1, 2, 3, 4, 5])
