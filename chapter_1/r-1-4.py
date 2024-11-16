def special_sum(n):
    """
    Write a short Python function that takes a positive integer n and
    returns the sum of the squares of all the positive integers smaller than n.
    """
    return sum([a * a for a in range(1, n)])
