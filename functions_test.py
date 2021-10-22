import functions as f
import random


def ans_u2q5(n):
    return n ** 3
    return n ** 3


def ans_u3q1(n):
    total = 0
    for i in range(1, n + 1):
        if i % 15 == 0:
            total += i

    return total
    return sum([i for i in range(1, n + 1) if i % 15 == 0])


def ans_u3q3(n):
    total = 0
    for i in range(1, n + 1):
        total += 1 / i

    return total
    return sum([1 / i for i in range(1, n + 1)])


def ans_u3q5(head, n):
    # I will not do that as I do not know how to do that
    for i in range(len(head)):
        if head[i] == i:
            return i
    return -1


def ans_u4q5(x, y=1):
    total = x + y
    if total > 20:
        return total
    else:
        return None


def ans_u4q8(nums):
    if len(nums) == 1:
        return nums[0]

    else:
        return nums[0] + ans_u4q8(nums[1:])


def test_func(num):
    a, b = 0, 1
    while True:
        a += b
        if a > num:
            return max(a, b)

        b += a

        if b > num:
            return max(a, b)

        print(a, b, end=" ")


if __name__ == "__main__":
    run_test = False

    if not run_test:
        print(test_func(13))
        exit()

    functions_to_test = ["u4q8"]
    passed = []

    try:
        if "u2q5" in functions_to_test:
            # Test cases for u2q5
            for i in range(-10, 11):
                ans = ans_u2q5(i)
                assert f.u2q5(i) == ans, f"u2q5: {i} should result in {ans}"
            passed.append("u2q5")

        if "u3q1" in functions_to_test:
            # Test cases for u3q1
            for i in range(-20, 100):
                ans = ans_u3q1(i)
                assert f.u3q1(i) == ans, f"u3q1: {i} should result in {ans}"
            passed.append("u3q1")

        if "u3q3" in functions_to_test:
            # Test cases for u3q3
            for i in range(-20, 100):
                ans = ans_u3q3(i)
                assert f.u3q3(i) == ans, f"u3q3: {i} should result in {ans}"
            passed.append("u3q3")

        if "u3q5" in functions_to_test:
            # Test cases for u3q5
            for i in range(100):
                head = sorted([random.randint(-50, 50) for i in range(10)])
                if random.randint(0, 10) > 8:
                    n = 51
                else:
                    n = random.choice(head)

                ans = ans_u3q5(head, n)
                assert f.u3q5(head, n) == ans, f"u3q5: list: {head}, {n} should result in {ans}"
            passed.append("u3q5")

        if "u4q5" in functions_to_test:
            # Test cases for u4q5
            for i in range(-20, 100):
                x, y = random.randint(-10, 20), random.randint(-10, 20)
                ans = ans_u4q5(x, y)
                assert f.u4q5(x, y) == ans, f"u4q5: {x}, {y} should result in {ans}"
            passed.append("u4q5")

        if "u4q8" in functions_to_test:
            for i in range(100):
                head = [random.randint(-50, 50) for i in range(10)]
                ans = ans_u4q8(head)
                assert f.u4q8(head) == ans, f"u4q8: list: {head} should result in {ans}"
            passed.append("u4q8")

        if "u4q8" in functions_to_test:
            for i in range(100):
                head = [random.randint(-50, 50) for i in range(10)]
                ans = ans_u4q8(head)
                assert f.u4q8(head) == ans, f"u4q8: list: {head} should result in {ans}"
            passed.append("u4q8")

    except AssertionError as e:
        print("\33[32m", end="")

        for passes in passed:
            print(f"{passes} worked")

        print("\33[31m", end="")
        print(e)
        print("\33[0m", end="")

    else:
        print("\33[32m", end="")
        print("SUCCESS")
        for passes in passed:
            print(f"{passes} tested")

        print("\33[0m", end="")