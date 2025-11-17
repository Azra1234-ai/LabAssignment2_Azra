def calculate_odd_even_sums(numbers):
    """
    Returns the sum of odd numbers and even numbers in the given list.
    """

    odd_sum = 0
    even_sum = 0

    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return odd_sum, even_sum


# Example usage
if __name__ == "__main__":
    data = [10, 21, 32, 43, 54, 65]

    odd_total, even_total = calculate_odd_even_sums(data)

    print("Original List:", data)
    print("Sum of Odd Numbers:", odd_total)
    print("Sum of Even Numbers:", even_total)

