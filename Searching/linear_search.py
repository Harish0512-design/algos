from typing import List


def linear_search(numbers_list: List[int], search_number: int) -> str:
    """
    Searches for a given number in a given list in a sequential manner.
    Args:
        numbers_list (List[int]): List of numbers.
    Returns:
        search_number (int): Number to search.
    """
    for i in range(len(numbers_list)):
        if numbers_list[i] == search_number:
            return f"Given number {search_number} found at index {i} in List/Array {numbers_list}."
    return "Number not found."
    

if __name__ == "__main__":
    input_numbers = list(
                        map(
                            lambda x: int(x), 
                            input(
                                "Enter number in a sequence separated with comma (,)\n (Eg: 2,1,3,42,4):\n"
                            ).split(',')
                        )
                    )
    input_number = int(input("Enter a number to search:\n"))
    result = linear_search(input_numbers, input_number)
    print(result)