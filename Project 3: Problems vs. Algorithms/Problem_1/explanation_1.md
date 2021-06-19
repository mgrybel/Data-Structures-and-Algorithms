In Problem 1, Square Root of an Integer, the requirement is that the time complexity must be in the order of O(log(n)). Therefore, the solution to this problem is implemented similarly to the binary search. 

In the beginning, the start is set to 1 (the minimum), and the end is set to a given number (the maximum value) since the square root of the given number will never be greater than that number. Next, we take the middle of the start and end, and check whether that is the square root. If it is not, the middle value will be either the start or the end depending on the quotient (if it is greater than or less than the given number, respectively). We continue performing the binary search until the start and end values are right next to one another. Finally, we return the smaller value since we are taking the floored value.

- The time complexity is O(log(n)) where n represents the number of elements.
- The space complexity is O(1) because we only store the start, middle, end and result as integer values. The use of memory is independent of the input.