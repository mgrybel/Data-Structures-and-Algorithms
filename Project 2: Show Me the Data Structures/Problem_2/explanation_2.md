In Problem 2, File Recursion, we do not know the directory structure, that is how many directories, subdirectories and files are beneath a provided path. Therefore, recursion was chosen to solve this problem. 

find_files operation:
- The time complexity of the find_files operation is O(mn) because the recursive function find_files needs to go through each directory within each of the sub-directories. Therefore, we have the time complexity O(mn) where m represents the number of sub-directories and n represents the number of files per directory.
- The space complexity of the find_files operation is also O(mn) - m represents the number of sub-directories within a directory and n represents the number of files that need to be stored.