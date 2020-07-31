if __name__ == "__main__":
    lst = [int(x) for x in input("Enter elements to the list : ").split()]
    print(sum(lst))


def sum(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum(lst[1:])
