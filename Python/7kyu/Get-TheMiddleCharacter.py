# Get the Middle Character

# You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

# If the string's length is odd, return the middle character.
# If the string's length is even, return the middle 2 characters.
# Examples:
# "test" --> "es"
# "testing" --> "t"
# "middle" --> "dd"
# "A" --> "A"


# My Solution:

def get_middle(s):
    length = len(s)
    middle = length // 2

    if length % 2 == 0:
        return s[middle - 1: middle + 1]
    else:
        return s[middle]