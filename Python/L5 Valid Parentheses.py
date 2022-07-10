# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. 
# The function should return true if the string is valid, and false if it's invalid.

# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints
# 0 <= input.length <= 100

# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters.
# Furthermore, the input string may be empty and/or not contain any parentheses at all.
# Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).

def valid_parentheses(string):
    parant = [x for x in string if x == "(" or x == ")"]
    has_open = 0
    has_close = 0
    for element in parant:
        if element == "(":
            has_open += 1
        else:
            has_close+= 1
        if has_close >has_open:
            return False # if more are closed then open at anytime return false
    return parant.count("(") == parant.count(")") #check to have equal number of open/close (more open will return false)
