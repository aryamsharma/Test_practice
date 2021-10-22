def u2q5(n):
    return n ** 3


def u3q1(n):
    return sum([i for i in range(1, n + 1) if i % 15 == 0])


def u3q3(n):
    return sum([1 / i for i in range(1, n + 1)])


def u3q5(head, n):
    for i in range(len(head)):
        if head[i] == i:
            return i
    return -1


def u4q5(x, y=1):
    total = x + y
    if total > 20:
        return total
    else:
        return None


def u4q8(nums):
    if len(nums) == 1:
        return nums[0]

    else:
        return nums[0] + u4q8(nums[1:])
