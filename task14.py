import itertools 
class fib1:
#"По объектам этого класса можно итерироваться и получать числа Фибоначчи"
    class _fib1_iter:
        #"Внутренний класс — итератор"
        def __init__(self):
            self.i = 1
            self.y = 1
        def __next__(self):
                a = self.i
                self.y = self.i+self.y
                self.i = self.y-self.i
                return a
    def __iter__(self):
        return fib1._fib1_iter()

f1 = fib1()
for p, f in zip(
    itertools.count(1),
    itertools.islice(f1, 100)
    ):
    print(f, p)
