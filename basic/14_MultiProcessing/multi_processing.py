import multiprocessing

sqrt_result = []


def calc_sqrt(nums):
    global sqrt_result
    for n in nums:
        # time.sleep(5)
        print("Square: ", n ** 2)
        sqrt_result.append(n ** 2)
    print("within the process: Result: ", sqrt_result)


def calc_cube(nums):
    for n in nums:
        # time.sleep(5)
        print("Cube: ", n ** 3)


if __name__ == "__main__":
    arr = [2, 3, 8, 9]
    p1 = multiprocessing.Process(target=calc_sqrt, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done!!")
    print("Result:", sqrt_result)
