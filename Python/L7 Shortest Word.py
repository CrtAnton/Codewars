# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

def find_short(s):
    return min(list(map(len, s.split(" "))))
    
    
# EXTRA, return the shortest word
def fint_short(s):
    min_len = min(list(map(len, s.split(" "))))
    return [x for x in s if len(x) == min_len][0]
