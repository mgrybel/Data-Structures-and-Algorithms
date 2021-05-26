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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

outgoing_calls = set()
incoming_calls = set()
outgoing_texts = set()
incoming_texts = set()

for data in calls:
    outgoing_calls.add(data[0])
    incoming_calls.add(data[1])

for data in texts:
    outgoing_texts.add(data[0])
    incoming_texts.add(data[1])

possible_telemarketers = sorted(outgoing_calls - (incoming_calls|outgoing_texts|incoming_texts))

print("These numbers could be telemarketers:")
for possible_telemarketer in possible_telemarketers:
    print(possible_telemarketer)
