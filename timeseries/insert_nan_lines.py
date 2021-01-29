# Utility to insert a NaN line at open time slots so that timeseries visualization shows an open space
# Transforms the file from stdin to stdout
from sys import stdin
from datetime import datetime, timedelta

def get_timestamp(line):
	return datetime.fromisoformat(line.split(' ')[0])

print(stdin.readline(), end='') # copy the header
first_data_line = stdin.readline()
print(first_data_line, end='')
previous = get_timestamp(first_data_line)
for line in stdin:
	current = get_timestamp(line)
	if ((current - previous).total_seconds() > 60):
		print((previous + timedelta(seconds=60)).isoformat()) # insert the NaN line
	print(line, end='')
	previous = current
