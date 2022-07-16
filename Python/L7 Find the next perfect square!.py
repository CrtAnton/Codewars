# If the parameter is itself not a perfect square then -1 should be returned. 
# You may assume the parameter is non-negative.

# Examples:(Input --> Output)

# 121 --> 144
# 625 --> 676
# 114 --> -1 since 114 is not a perfect square

def find_next_square(sq):
    return ((sq**0.5)+1)**2 if sq**0.5 == int(sq**0.5) else -1
