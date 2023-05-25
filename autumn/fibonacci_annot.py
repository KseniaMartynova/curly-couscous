"""Программа, выдающая члены последовательности Фибоначчи"""

import itertools
from typeguard import typechecked


class fib1:
    """По объектам этого класса можно
    итерироваться и получать числа Фибоначчи"""

    class _fib1_iter:
        """Внутренний класс — итератор"""
        @typechecked
        def __init__(self) -> None:
            self.i: int = 1
            self.y: int = 1

        @typechecked
        def __next__(self) -> int:
            a: int = self.i
            self.y = self.i+self.y
            self.i = self.y-self.i
            return a

    def __iter__(self):
        return fib1._fib1_iter()


f1: fib1 = fib1()
for p, f in zip(itertools.count(1), itertools.islice(f1, 100)):
    print(f, p)
