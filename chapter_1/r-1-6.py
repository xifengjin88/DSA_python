def odd_squares_sum(n):
    """
    Write a short Python function that takes a positive integer n and
    returns the sum of the squares of all the odd positive integers smaller than n.
    """
    return sum((a * a for a in range(1, n) if a % 2 == 1))


def test_odd_squares_sum():
    """Test function for summing squares of odd positive integers smaller than n."""

    # Test Case 1: n = 1 (no odd numbers smaller than 1)
    assert odd_squares_sum(1) == 0, "Failed for n=1"

    # Test Case 2: n = 2 (only 1 is odd and smaller than 2)
    assert odd_squares_sum(2) == 1, "Failed for n=2: should be 1² = 1"

    # Test Case 3: n = 3 (only 1 is odd and smaller than 3)
    assert odd_squares_sum(3) == 1, "Failed for n=3: should be 1² = 1"

    # Test Case 4: n = 4 (1 and 3 are odd and smaller than 4)
    assert odd_squares_sum(4) == 10, "Failed for n=4: should be 1² + 3² = 1 + 9 = 10"

    # Test Case 5: n = 6 (1, 3, 5 are odd and smaller than 6)
    assert odd_squares_sum(6) == 35, "Failed for n=6: should be 1² + 3² + 5² = 1 + 9 + 25 = 35"

    # Test Case 6: n = 10 (1, 3, 5, 7, 9 are odd and smaller than 10)
    assert odd_squares_sum(10) == 165, "Failed for n=10: should be 1² + 3² + 5² + 7² + 9² = 1 + 9 + 25 + 49 + 81 = 165"

    # Edge Case 7: Large number
    assert odd_squares_sum(100) > 0, "Failed for large number"

    print("All test cases passed!")


# Helper function to manually verify calculations
def show_work(n):
    """Shows the detailed calculation for a given n"""
    odds = [i for i in range(1, n) if i % 2 == 1]
    squares = [i * i for i in odds]
    print(f"n = {n}")
    print(f"Odd numbers smaller than {n}: {odds}")
    print(f"Their squares: {squares}")
    print(f"Sum: {sum(squares)}")
    print("---")


if __name__ == '__main__':
    # Show detailed calculations for first few cases
    test_odd_squares_sum()
