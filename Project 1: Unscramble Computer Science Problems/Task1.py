"""
Read file into texts and calls.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

distinct_numbers = set()

for data in texts:
    distinct_numbers.add(data[0])
    distinct_numbers.add(data[1])

for data in calls:
    distinct_numbers.add(data[0])
    distinct_numbers.add(data[1])

print("There are {0} different telephone numbers in the records.".format(len(distinct_numbers)))
