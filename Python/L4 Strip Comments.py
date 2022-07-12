# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. 
# Any whitespace at the end of the line should also be stripped out.

# Example:

# Given an input string of:

# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:

# apples, pears
# grapes
# bananas

def strip_comments(strng, markers):
    string_list = strng.split("\n")
    new_list = []
    for item in string_list:
        sequence = ""
        for character in item:
            if character not in markers:
                sequence += character
            else:
                break
        new_list.append(sequence.rstrip())
    return "\n".join(new_list)
            
            
            
