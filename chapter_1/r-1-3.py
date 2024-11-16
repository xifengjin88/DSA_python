def minmax(data):
    """
    Write a short Python function, minmax(data),
    that takes a sequence of one or more numbers,
    and returns the smallest and largest numbers,
    in the form of a tuple of length two.
    Do not use the built-in functions min or max in implementing your solution.
    """

    smallest = float("inf")
    largest = float("-inf")
    for i in data:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i
    return smallest, largest
