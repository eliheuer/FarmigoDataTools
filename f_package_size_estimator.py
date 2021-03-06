#!
import csv              #!  Comma-Separated Values -- tabular data in plain text.
import re               #!  Regular Expressions -- text matching patterns.
import os               #!  Miscellaneous operating system interfaces.
import sys              #!  System-specific parameters and functions.
from time import sleep  #!  Sleep -- for command-line animation.

#! Function for printing slowly (animation) -- ex: print_slowly ('Hello World!')
def print_slowly(text):
    for glyph in text:
        print glyph,
        sys.stdout.flush() #! I'm not sure if this is necesarry.
        sleep(0.05)

#! Let the user know it's working, slowly.
print ''
print_slowly ('## farmigotools\n## ft_package_size_estimator.py')


#! Loop through every file in the current working directory
for csv_input_filename in os.listdir('.'):
    if not csv_input_filename.endswith('.csv'):
        continue # skip non-csv files
    print ''
    print 'Processing -- ' + csv_input_filename + '...'
    print ''

    #! Print column headers
    csv_input_file = open(csv_input_filename)
    csv_output_file = open(os.path.join(output_dir, csv_input_filename), 'w')
    csv_reader = csv.reader(csv_input_file)
    csv_writer = csv.writer(csv_output_file)


print_slowly ('## DONE!')
print ('')
print ('')
