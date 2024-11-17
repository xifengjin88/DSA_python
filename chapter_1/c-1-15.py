def is_distinct(nums):
    """
    Write a Python function that takes a sequence of numbers and determines
    if all the numbers are different from each other (that is, they are distinct).
    """
    return len(set(nums)) == len(nums)
