# Problem 4: Dutch National Flag Problem


def sort_012(input_list):
    """
    Given an input array consisting of only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    start = 0
    end = len(input_list) - 1
    current_index = 0

    while current_index <= end:
        if input_list[current_index] == 0:
            input_list[current_index] = input_list[start]
            input_list[start] = 0
            start += 1
            current_index += 1
        elif input_list[current_index] == 1:
            current_index += 1
        elif input_list[current_index] == 2:
            input_list[current_index] = input_list[end]
            input_list[end] = 2
            end -= 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# Test Cases

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])                                                # prints Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])   # prints Pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])                        # prints Pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])                        # prints Pass
test_function([0, 0, 0, 0, 0, 0])                                                               # prints Pass
test_function([1, 1, 1, 1, 1, 1])                                                               # prints Pass
test_function([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])                                          # prints Pass
test_function([0, 0, 2, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0])   # prints Pass
test_function([])                                                                               # prints Pass