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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

time_dict = {}

for data in calls:
    if data[0] in time_dict:
        time_dict[data[0]] += int(data[3])
    else:
        time_dict[data[0]] = int(data[3])

    if data[1] in time_dict:
        time_dict[data[1]] += int(data[3])
    else:
        time_dict[data[1]] = int(data[3])

longest_time = max(time_dict, key=lambda x: time_dict[x])

print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(longest_time, time_dict[longest_time]))
