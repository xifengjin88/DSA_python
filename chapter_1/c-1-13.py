def reverse(nums):
    """
    Write a pseudo-code description of a function that reverses a list of n integers, so that the numbers are listed in the opposite order than they were before,
    and compare this method to an equivalent Python function for doing the same thing.

    """
    if len(nums) == 0:
        return nums
    return [nums[i] for i in range(len(nums) - 1, -1, -1)]


def test_reverse_nums():
    assert reverse([]) == [], "Failed for []"

    assert reverse([1, 2, 3, 4]) == [4, 3, 2, 1], "Failed for [1,2,3,4]"

    print("All test cases passed!")


if __name__ == "__main__":
    test_reverse_nums()