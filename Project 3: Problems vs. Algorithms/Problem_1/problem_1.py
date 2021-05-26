# Problem 1: Square Root of an Integer


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None or type(number) != int:
        return "Please enter a positive integer value"

    if number < 0:
        return "Please enter a positive integer value"

    if number == 0 or number == 1:
        return number

    start = 1
    end = number

    while start <= end:
        middle = (start + end) // 2
        middle_squared = middle * middle

        if middle_squared == number:
            return middle
        elif middle_squared > number:
            end = middle - 1
        elif middle_squared < number:
            start = middle + 1
            result = middle
    
    return result


# Test Cases

print ("Pass" if  (3 == sqrt(9)) else "Fail")           # prints Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail")           # prints Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail")          # prints Pass
print ("Pass" if  (1 == sqrt(1)) else "Fail")           # prints Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail")          # prints Pass
print ("Pass" if  (8 == sqrt(81)) else "Fail")          # prints Fail
print("Pass" if (9999 == sqrt(99999999)) else "Fail")   # prints Pass

print("sqrt(None): {}".format(sqrt(None)))              # prints sqrt(None): Please enter a positive integer value
print("sqrt(-3): {}".format(sqrt(-3)))                  # prints sqrt(-3): Please enter a positive integer value
print("sqrt(1.25): {}".format(sqrt(1.25)))              # prints sqrt(1.25): Please enter a positive integer value
print("sqrt(0): {}".format(sqrt(0)))                    # prints sqrt(0): 0
print("sqrt(1): {}".format(sqrt(1)))                    # prints sqrt(1): 1
print("sqrt(9): {}".format(sqrt(9)))                    # prints sqrt(9): 3
print("sqrt(16): {}".format(sqrt(16)))                  # prints sqrt(16): 4
print("sqrt(27): {}".format(sqrt(27)))                  # prints sqrt(27): 5
print("sqrt(225): {}".format(sqrt(225)))                # prints sqrt(225): 15