import time


def execution_time(func):
    def inner(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        print(f"Time Taken for execution {et - st} Seconds")
        return res
    return inner


@execution_time
def bubble_sort(lst: list) -> list:
    n = len(lst)

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break

    return lst


if __name__ == "__main__":
    lst = [78, 2, 32, 839, 778, 87, 2, 182, 93]

    print(bubble_sort(lst))

    alphabet_lst = ["Shravan", "Nagendra", "Rupesh", "harish", "Mazahar", "Prabhakar", "Balaji", "Vinod"]

    print(bubble_sort(alphabet_lst))
