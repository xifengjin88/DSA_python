import string


def remove_punctuation(text):
    """
    Write a short Python function that takes a string s,
    representing a sentence, and returns a copy of the string
    with all punctuation removed. For example,
    if given the string "Let s try, Mike.", this function would return "Lets try Mike".
    """

    copy = text

    for char in text:
        if char in string.punctuation:
            copy = copy.replace(char, "")
    return copy


print(remove_punctuation("Let's try, Mike."))
