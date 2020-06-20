def second_min(students):
    _min = min(students, key=lambda x: x[1])
    students = list(filter(lambda a: a[1] != _min[1], students))
    print(students)
    _min = min(students, key=lambda x: x[1])
    result = []
    for pair in students:
        if (pair[1] == _min[1]):
            result.append(pair)
    return sorted(result)


if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    for name in second_min(students):
        print(name[0])
