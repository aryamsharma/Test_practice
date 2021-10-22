import functions as f
import random as r
import string as s


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


def ans_u4q9(nums):
    if len(nums) == 1:
        return nums[0]

    else:
        return nums[0] + ans_u4q9(nums[1:])


def ans_u4q10(sentence):
    sentence = "".join([i for i in sentence if i != " "]).lower()
    return sentence == sentence[::-1]


def ans_u5q7(n):
    return [i for i in range(-n, n + 1)]


def ans_u5q9(head):
    return [i for i in head if i.lower().count("e") == 0]


def ans_u5q10(head):
    return sorted([len(i) for i in head])


class Tools:
    def create_string():
        string_list = "".join(r.choices(s.ascii_letters, k=r.randint(1, 50)))
        return string_list


if __name__ == "__main__":
    functions_to_test = ["u2q5", "u3q1", "u3q3", "u3q5", "u4q5", "u4q9", "u4q10", "u5q7", "u5q9", "u5q10"]
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
                head = sorted([r.randint(-50, 50) for i in range(10)])
                if r.randint(0, 10) > 8:
                    n = 51
                else:
                    n = r.choice(head)

                ans = ans_u3q5(head, n)
                assert f.u3q5(head, n) == ans, f"u3q5: list: {head}, {n} should result in {ans}"
            passed.append("u3q5")

        if "u4q5" in functions_to_test:
            # Test cases for u4q5
            for i in range(-20, 100):
                x, y = r.randint(-10, 20), r.randint(-10, 20)
                ans = ans_u4q5(x, y)
                assert f.u4q5(x, y) == ans, f"u4q5: {x}, {y} should result in {ans}"
            passed.append("u4q5")

        if "u4q9" in functions_to_test:
            for i in range(100):
                head = [r.randint(-50, 50) for i in range(10)]
                ans = ans_u4q9(head)
                assert f.u4q9(head) == ans, f"u4q9: list: {head} should result in {ans}"
            passed.append("u4q9")

        if "u4q10" in functions_to_test:
            for word in ["Taco Cat", "Racecar", "randomstring"]:
                ans = ans_u4q10(word)
                assert f.u4q10(word) == ans, f"u4q10: {word} should result in {ans}"
            passed.append("u4q10")

        if "u5q7" in functions_to_test:
            for i in range(0, 10):
                ans = ans_u5q7(i)
                assert f.u5q7(i) == ans, f"u5q7: {i} should result in {ans}"
            passed.append("u5q7")

        if "u5q9" in functions_to_test:
            for i in range(10):
                head = [Tools.create_string() for i in range(r.randint(1, 5))]
                ans = ans_u5q9(head)
                assert f.u5q9(head) == ans, f"u5q9: {head} should result in {ans}"
            passed.append("u5q9")

        if "u5q10" in functions_to_test:
            for i in range(10):
                head = [Tools.create_string() for i in range(r.randint(1, 5))]
                ans = ans_u5q10(head)
                assert f.u5q10(head) == ans, f"u5q10: {head} should result in {ans}"
            passed.append("u5q10")

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
