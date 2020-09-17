# Problem 6: Unsorted Integer Array


import random

def get_min_max(ints):
   """
   Return a tuple(min, max) out of list of unsorted integers.

   Args: ints(list): list of integers containing one or more integers
   """
   if len(ints) == 0:
      return None

   min = ints[0]
   max = ints[0]
   
   for num in ints:
      if num > max:
         max = num
      elif num < min:
         min = num

   return (min, max)


# Test Cases

# Ten Integers
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")                   # prints: Pass
print(f"get_min_max(l): {get_min_max(l)}")                                 # prints: get_min_max(l): (0, 9)

# Empty List
print ("Pass" if (None == get_min_max([])) else "Fail")                    # prints: Pass
print(f"get_min_max([]): {get_min_max([])}")                               # prints: get_min_max([]): None

# Repeated Numbers
print ("Pass" if ((5, 5) == get_min_max([5,5,5,5])) else "Fail")           # prints: Pass
print(f"get_min_max([5,5,5,5]): {get_min_max([5,5,5,5])}")                 # prints: get_min_max([5,5,5,5]): (5, 5)

# Negative Values
print ("Pass" if ((-3, 12) == get_min_max([12,9,-3,1,4,6])) else "Fail")   # prints: Pass
print(f"get_min_max([12,9,-3,1,4,6]): {get_min_max([12,9,-3,1,4,6])}")     # prints: get_min_max([12,9,-3,1,4,6]): (-3, 12)