# Problem 2: Search in a Rotated Sorted Array


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if number is None or type(number) != int:
        return -1
    return rotated_array_search_recursive(input_list, number, 0, len(input_list) - 1)


def rotated_array_search_recursive(input_list, number, start, end):
    if start > end:
        return -1

    middle_index = (start + end) // 2
    middle_element = input_list[middle_index]

    if middle_element == number:
        return middle_index

    if input_list[start] <= middle_element:
        if number == input_list[start]:
            return start
        elif number == middle_element:
            return middle_index
        elif number > input_list[start] and number < middle_element:
            return rotated_array_search_recursive(input_list, number, start, middle_index - 1)
        
        return rotated_array_search_recursive(input_list, number, middle_index + 1, end)

    if number == input_list[end]:
        return end

    if number == middle_element:
        return middle_index

    if number < input_list[end] and number > middle_element:
        return rotated_array_search_recursive(input_list, number, middle_index + 1, end)

    return rotated_array_search_recursive(input_list, number, start, middle_index - 1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


# ---------- Tests ----------

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# Default test cases
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])    # prints Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])    # prints Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])           # prints Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])           # prints Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])          # prints Pass

# Other combinations
test_function([[1, 2, 3, 4], 3])                    # prints Pass
test_function([[6, 7, 8, 1, 2, 3, 4], None])        # prints Pass
test_function([[6, None, 8, 1, None, 3, 4], None])  # prints Fail

# An array with a single value
test_function([[1], 0])                             # prints Pass
test_function([[1], 1])                             # prints Pass

# An empty array
test_function([[], 8])                              # prints Pass

# A non-rotated array
test_function([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 3]) # prints Pass

print(f"rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6): {rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6)}") # prints rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6): 0
print(f"rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1): {rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1)}") # prints rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1): 5
print(f"rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8): {rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8)}") # prints rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8): 2
print(f"rotated_array_search([6, 7, 8, 1, 2, 3, 4], 1): {rotated_array_search([6, 7, 8, 1, 2, 3, 4], 1)}") # prints rotated_array_search([6, 7, 8, 1, 2, 3, 4], 1): 3
print(f"rotated_array_search([6, 7, 8, 1, 2, 3, 4], 10): {rotated_array_search([6, 7, 8, 1, 2, 3, 4], 10)}") # prints rotated_array_search([6, 7, 8, 1, 2, 3, 4], 10): -1
print(f"rotated_array_search([1, 2, 3, 4], 3): {rotated_array_search([1, 2, 3, 4], 3)}") # prints rotated_array_search([1, 2, 3, 4], 3): 2
print(f"rotated_array_search([6, 7, 8, 1, 2, 3, 4], None): {rotated_array_search([6, 7, 8, 1, 2, 3, 4], None)}") # prints rotated_array_search([6, 7, 8, 1, 2, 3, 4], None): -1
print(f"rotated_array_search([6, None, 8, 1, None, 3, 4], None): {rotated_array_search([6, None, 8, 1, None, 3, 4], None)}") # prints rotated_array_search([6, None, 8, 1, None, 3, 4], None): -1