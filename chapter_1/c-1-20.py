from random import randint


def shuffle(nums):
    """
    Python’s random module includes a function shuffle(data) that accepts
    a list of elements and randomly reorders the elements so that each possible
    order occurs with equal probability. The random module includes a
    more basic function randint(a, b)
    that returns a uniformly random integer from a to b
    (including both endpoints). Using only the randint function,
    implement your own version of the shuffle function.
    """

    nums = nums.copy()
    for i in range(len(nums) - 1, 0, -1):
        j = randint(0, i)
        nums[i], nums[j] = nums[j], nums[i]
    return nums


print(shuffle([1, 2, 3, 4, 5]))