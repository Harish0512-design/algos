# find the min value and swap it with first value.
def selection_sort(lst: list) -> list:
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[min_idx] > lst[j]:
                min_idx = j

        lst[min_idx], lst[i] = lst[i], lst[min_idx]

    return lst


if __name__ == "__main__":
    lst = [89, 2829, 17, 792, 9181, 821]

    print(selection_sort(lst))
