# Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
# Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    return " ".join([(word[1:]+word[0]+"ay") if word[0].isalpha() else (word) for word in text.split(" ") ])
# A bit unclear at a first look, I actually did it in 4 lines and refractor them in 1 line.(just to push it for that 1 line solution)
