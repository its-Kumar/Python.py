"""
Sharing data between multiple processes.
"""
import multiprocessing

numbers = [1, 2, 3, 43, 5, 6, 7]


def calc_sqrt(nums, result, v):
    # assigning value inside process
    v.value = 5.678
    for idx, n in enumerate(nums):
        #time.sleep(5)
        print("Square: ", n**2)
        result[idx] = (n**2)
    print("within the process: Result: ", result[:])


if __name__ == "__main__":
    # shared memory
    result = multiprocessing.Array('i', len(numbers))

    # shared value
    v = multiprocessing.Value('d', 0.0)

    p = multiprocessing.Process(target=calc_sqrt, args=(numbers, result, v))
    p.start()
    p.join()

    print("Outside process:", result[:])
    print("Value outside the process:", v.value)
