"""
Parallel processing
"""
import time
from multiprocessing import Pool


def f(n):
    sum = 0
    for x in range(1000):
        sum += x * x
    return sum
    #return n * n


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    t1 = time.time()
    p = Pool()
    #result = p.map(f, array)
    result = p.map(f, range(100000))
    #print(result)
    p.close()
    p.join()
    print("Pool Took:", time.time() - t1)

    t2 = time.time()
    result = []
    for x in range(100000):
        result.append(f(x))

    print("Serial Processing took:", time.time() - t2)
