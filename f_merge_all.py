#!
import csv              #!  Comma-Separated Values - tabular data in plain text.
import os               #!  Miscellaneous operating system interfaces.
import sys              #!  System-specific parameters and functions.
from time import sleep  #!  Sleep - for command-line animation.

#! Function for printing slowly (animation) -- ex: print_slowly ('Hello World!')
def print_slowly(text):
    for glyph in text:
        print glyph,
        sys.stdout.flush() #! I'm not sure if this is necesarry.
        sleep(0.05)

#! Let the user know it's working, slowly.
print ''
print_slowly ('farmigotools\n\nft_merge_all.py')
print ''
print ''
sleep(0.3)

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

    #! create variables from csv
    for row in csv_reader:



        csv_writer.writerow(output_row)
    csv_output_file.close()



fout=open("out.csv","a")
# first file:
for line in open("sh1.csv"):
    fout.write(line)
# now the rest:
for num in range(2,201):
    f = open("sh"+str(num)+".csv")
    f.next() # skip the header
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()



#! Let the user know it's done
print_slowly ('## DONE!')
print ('')
print ('')
