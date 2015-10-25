#
import csv              #!  Comma-Separated Values - tabular data in plain text.
import os               #!  Miscellaneous operating system interfaces.
import sys              #!  System-specific parameters and functions.

csv_reader = csv.reader(sys.stdin)
csv_writer = csv.writer(sys.stdout)

# remove blank lines from input csv
for row in csv_reader:
    if any(field.strip() for field in row):
        csv_writer.writerow(row)
