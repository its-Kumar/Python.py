"""
Sharing memory using queue
"""
import multiprocessing
numbers = [1, 2, 3, 43, 5, 6, 7]


def calc_sqrt(nums, q):
    for n in nums:
        #time.sleep(5)
        print("Square: ", n**2)
        q.put(n**2)


if __name__ == "__main__":

    # shared queue
    q = multiprocessing.Queue()

    p = multiprocessing.Process(target=calc_sqrt, args=(numbers, q))
    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())
