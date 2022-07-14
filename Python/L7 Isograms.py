# An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
# Implement a function that determines whether a string that contains only letters is an isogram. 
# Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true
# "aba" --> false
# "moOse" --> false (ignore letter case)

def is_isogram(string):
    results = [False if string.lower().count(c)>1 else True for c in string.lower()]
    return False not in results 

# Solution above is overkill...seen the solution after submitting

# def is_isogram(string):
#     return len(string) == len(set(string.lower()))
