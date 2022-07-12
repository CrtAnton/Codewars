# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. 
# ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. 
# If there are numbers or special characters included in the string, they should be returned as they are. 
# Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.

def rot13(message):
    new = ""
    for letter in message:
        if letter.islower():
            new += chr(ord("a") + (ord(letter)-ord("a")+13)%26)
        elif letter.isupper():
            new += chr(ord("A") + (ord(letter)-ord("A")+13)%26)
        else:
            new += letter
    return new
