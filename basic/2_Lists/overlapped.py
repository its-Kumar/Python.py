"""Given a collection of intervals, merge all overlapping intervals.
Input: [[1,3],[2,6],[8,10], [9,11] ,[10,12], [2,4] ,[15,18]]
Output: [[1,6],[8,12],[15,18]] """


def overlapped(input_):
    input_ = sorted(input_, key=lambda x: x[0])
    for j in range(2):
        i = 0
        while i < len(input_) - 1:
            if input_[i][-1] > input_[i + 1][0]:
                input_[i + 1] = [min(input_[i][0], input_[i + 1][0]),
                                 max(input_[i][-1], input_[i + 1][-1])]
                input_.pop(i)
            i += 1

    # for i in range(len(input)):
    #     start = input[i][0]
    #     end = input[i][-1]
    #     start2 = output[-1][0]
    #     end2 = output[-1][1]

    #     if start > end2:
    #         # output.pop(-1)
    #         output.append([start, end2])

    #     else:
    #         output[-1][-1] = max(output[-1][-1], end)

    return input_


print(overlapped(
    [[1, 3], [2, 6], [8, 10], [9, 11], [10, 12], [2, 4], [15, 18]]))
