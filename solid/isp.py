from abc import ABC, abstractmethod


class Mammals(ABC):
    @abstractmethod
    def swim(self) -> bool:
        print("Can't swim")

    def walk(self) -> bool:
        print("Can't walk")


class Human(Mammals):
    def swim(self):
        return print("Humans can swim")

    def walk(self):
        return print("Humans can walk")


class Whales(Mammals):
    def swim(self):
        return print("Whales can swim")


if __name__ == "__main__":
    _ = None
    Human.swim(_)
    Human.walk(_)
    Whales.swim(_)
    Whales.walk(_)



