def str_permutations(letters=None):
    """
    Write a Python program that outputs all possible strings formed
    by using the characters c , a , t , d , o ,and g exactly once.
    """
    if letters is None:
        letters = ["c", "a", "t", "d"]

    permutations = []

    for i in range(len(letters)):
        first_letter = [i]

        for j in range(len(letters)):
            if j not in first_letter:
                second_letter = first_letter.copy()
                second_letter.append(j)
                for k in range(len(letters)):
                    if k not in second_letter:
                        third_letter = second_letter.copy()
                        third_letter.append(k)

                        for a in range(len(letters)):
                            if a not in third_letter:
                                last_letter = third_letter.copy()
                                last_letter.append(a)
                                permutations.append("".join([letters[idx] for idx in last_letter]))

    return permutations
