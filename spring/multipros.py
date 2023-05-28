'программа проверяет большие числа на то, являются ли они полными квадратами'


import time
import multiprocessing

def is_square(a):
    b = a ** 0.5
    if b - int(b) == 0:
        return True
    else:
        return False

def test_all(pool):
    l = pool.map(is_square, range(500_000_000, 500_005_000))
    return l

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    t0 = time.time()
    print(test_all(pool))
    print("Time spent:", time.time() - t0)
else:
    print("__name__:", __name__)