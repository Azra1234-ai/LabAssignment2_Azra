def sum_of_squares(numbers):
    """
    Calculate the sum of squares of numbers in a list.

    Args:
        numbers: A list of numbers (integers or floats)

    Returns:
        The sum of squares of all numbers in the list

    Example:
        >>> sum_of_squares([1, 2, 3])
        14
        >>> sum_of_squares([2, 4, 6])
        56
    """
    return sum(x ** 2 for x in numbers)


# Example usage
if __name__ == "__main__":
    # Test cases
    test_list1 = [1, 2, 3]
    test_list2 = [2, 4, 6]
    test_list3 = [5]
    test_list4 = []

    print(f"Sum of squares of {test_list1}: {sum_of_squares(test_list1)}")
    print(f"Sum of squares of {test_list2}: {sum_of_squares(test_list2)}")
    print(f"Sum of squares of {test_list3}: {sum_of_squares(test_list3)}")
    print(f"Sum of squares of {test_list4}: {sum_of_squares(test_list4)}")
