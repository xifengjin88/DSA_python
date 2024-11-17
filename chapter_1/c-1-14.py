def has_odd_product_pair(nums):
    """
    Write a short Python function that takes a sequence of integer values and determines
    if there is a distinct pair of numbers in the sequence whose product is odd.
    """
    num_seen = set()
    for num in nums:
        if num % 2 == 1:
            if num_seen and num not in num_seen:
                return True
            num_seen.add(num)

    return False


def test_odd_product_pair():
    # Test Case 1: Basic case with an odd product pair
    assert has_odd_product_pair([1, 3, 2, 4]) == True, \
        "Failed: Should return True for sequence [1, 3, 2, 4] as 1 * 3 = 3 (odd)"

    # Test Case 2: No odd product pairs
    assert has_odd_product_pair([2, 4, 6, 8]) == False, \
        "Failed: Should return False for all even numbers as their products will always be even"

    # Test Case 3: Empty sequence
    assert has_odd_product_pair([]) == False, \
        "Failed: Empty sequence should return False as there are no pairs to check"

    # Test Case 4: Single number
    assert has_odd_product_pair([1]) == False, \
        "Failed: Single number sequence should return False as we need at least two numbers"

    # Test Case 5: All odd numbers
    assert has_odd_product_pair([1, 3, 5, 7]) == True, \
        "Failed: Should return True for sequence of odd numbers as any pair will have odd product"

    # Test Case 6: Duplicate numbers
    assert has_odd_product_pair([1, 1, 2]) == False, \
        "Failed: Should return False for [1, 1, 2] as pairs must be distinct"

    # Test Case 7: Negative numbers
    assert has_odd_product_pair([-1, -3, 2, 4]) == True, \
        "Failed: Should return True as (-1) * (-3) = 3 is odd"

    print("All test cases passed!")


if __name__ == "__main__":
    test_odd_product_pair()
