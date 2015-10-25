#
import csv              #!  Comma-Separated Values - tabular data in plain text.
import os               #!  Miscellaneous operating system interfaces.
import sys              #!  System-specific parameters and functions.
from time import sleep  #!  Sleep - for command-line animation.

# Function for printing slowly (animation) -- ex: print_slowly ('Hello World!')
def print_slowly(text):
    for glyph in text:
        print glyph,
        sys.stdout.flush() #! I'm not sure if this is necesarry.
        sleep(0.05)

# Let the user know it's working, slowly.
print ''
print_slowly ('farmigotools\n\n' + sys.argv[0])
print ''
print ''
sleep(0.3)

# Make a new folder in the current directory for the outputed files.
output_dir = 'CSVs_4_route4me'
print ''
print ''
print 'Making a new folder called -- ' + output_dir
sleep(0.3)
try:
    os.makedirs(output_dir)
except OSError:
    # Directory already exists, move on.
    pass

# Loop through every file in the current working directory
for csv_input_filename in os.listdir('.'):
    if not csv_input_filename.endswith('.csv'):
        continue # skip non-csv files
    print ''
    print 'Processing -- ' + csv_input_filename + '...'
    print ''

    # Print column headers
    csv_input_file = open(csv_input_filename)
    csv_output_file = open(os.path.join(output_dir, csv_input_filename), 'w')
    csv_reader = csv.reader(csv_input_file)
    csv_writer = csv.writer(csv_output_file)

    # create variables from csv
    for row in csv_reader:
        #bag_type = row[1]
        last_name = row[2]
        first_name = row[3]
        primary_phone = row[4]
        secondary_phone = row[5]
        address = row[7]
        city = row[8]
        state = row[9]
        zipcode = row[10]
        blank = None

        # output reformated CSV
        output_row = [
        address + ' ' + city + ' ' + state + ' ' + zipcode,
        first_name + ' ' + last_name + ' | ' +
        primary_phone + ' | ' + secondary_phone,
        'Run 1']
        csv_writer.writerow(output_row)
    csv_output_file.close()

# Let the user know it's done
print_slowly ('## DONE!')
print ('')
print ('')
