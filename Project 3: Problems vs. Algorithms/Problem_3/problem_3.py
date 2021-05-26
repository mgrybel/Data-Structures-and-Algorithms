# Problem 3: Rearrange Array Digits


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_values = merge_sort(input_list)
    return join(sorted_values)


def merge_sort(input_list):
    """
    Sort a given array in a descending order using the Merge Sort algorithm
    """
    if len(input_list) <= 1:
        return input_list

    middle = len(input_list) // 2
    left = input_list[middle:]
    right = input_list[:middle]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

    
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged


def join(sorted_values):
    values = [0, 0]
    for i, j in enumerate(sorted_values):
        values[i % 2] = values[i % 2] * 10 + j
    return values


# ---------- Tests ----------

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Default test cases
test_function([[1, 2, 3, 4, 5], [542, 31]])                 # prints Pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])             # prints Pass

# The same numbers and repeated numbers
test_function([[0, 0], [0, 0]])                             # prints Pass
test_function([[5, 5, 5, 5, 5, 5], [555, 555]])             # prints Pass
test_function([[1, 1, 2, 2, 3, 3, 4, 4], [4321, 4321]])     # prints Pass

# Not sorted array, no repeated numbers
test_function([[9, 1, 8, 2, 7, 3, 9], [9831, 972]])         # prints Pass


print(f"rearrange_digits([1, 2, 3, 4, 5]): {rearrange_digits([1, 2, 3, 4, 5])}")                    # prints rearrange_digits([1, 2, 3, 4, 5]): [531, 42]
print(f"rearrange_digits([4, 6, 2, 5, 9, 8]): {rearrange_digits([4, 6, 2, 5, 9, 8])}")              # prints rearrange_digits([4, 6, 2, 5, 9, 8]): [964, 852]
print(f"rearrange_digits([0, 0]): {rearrange_digits([0, 0])}")                                      # prints rearrange_digits([0, 0]): [0, 0]
print(f"rearrange_digits([5, 5, 5, 5, 5, 5]): {rearrange_digits([5, 5, 5, 5, 5, 5])}")              # prints rearrange_digits([5, 5, 5, 5, 5, 5]): [555, 555]
print(f"rearrange_digits([1, 1, 2, 2, 3, 3, 4, 4]): {rearrange_digits([1, 1, 2, 2, 3, 3, 4, 4])}")  # prints rearrange_digits([1, 1, 2, 2, 3, 3, 4, 4]): [4321, 4321]
print(f"rearrange_digits([9, 1, 8, 2, 7, 3, 9]): {rearrange_digits([9, 1, 8, 2, 7, 3, 9])}")        # prints rearrange_digits([9, 1, 8, 2, 7, 3, 9]): [9831, 972]