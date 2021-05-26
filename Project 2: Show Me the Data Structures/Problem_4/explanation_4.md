In Problem 4, Active Directory, we do not know the group structure, that is how many groups we would have to search. Therefore, recursion was chosen to solve this problem.

is_user_in_group operation:
- The time complexity of the is_user_in_group operation is O(mn) because when searching for a user, we start at a current group and check if the user we are looking for is there. If we determine, that the user is not in that group, we need to use recursion and search through each of the sub-groups and check if the user we are looking for is there. This gives us the time complexity of O(mn), where m represents the number of sub-groups and n represents the number of users. 
- The space complexity of the is_user_in_group operation is also O(mn) - m represents the number of sub-groups within a group and n represents the number of users.