# Complete the function scramble(str1, str2) that returns true if a portion of str1 
# characters can be rearranged to match str2, otherwise returns false.

# Notes:

# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

# FIRST ATTEMPT PASSED ALL TESTS EXCEPT PERFORMANCE TEST...
# def scramble(s1, s2):
#     s1_list = [x for x in s1]
#     s2_list = [x for x in s2]
#     for letter in s2_list:
#         if letter in s1_list:
#             s1_list.remove(letter)
#         else:
#             return False
#     return True

# SECOND ATTEMPT SAME AS BEFORE
# def scramble(s1, s2):
#     for letter in s2:
#         if s1.count(letter) < s2.count(letter):
#             return False
#     return True

# THiRD ATTEMPT

def scramble(s1, s2):
    for letter in set(s2):# WHEN reaching performace test(strings with 600000 chars) checks just once for each letter instead 600000 times
        if s1.count(letter) < s2.count(letter):
            return False
    return True
