# Concordance
Main idea: code written in Python that tackles a version of concordance known as keyword in context. 
Note: This project was completed as an assignment requirement for UVic's SENG-265. The below 'explanation' has been provided from Dr. Michael Zastre's assignment description.

The Oxford English Dictionary defines a concordance is an “alphabeticalarrangement of principal words contained in a book, with citations of the passagesin which they occur”. Someone using a concordance is therefore able to look up aword of interest to them for that book, and find all the locations (page numbers andline numbers) where the word is used


This project is an implementation of the concept "keyword in context" in Python 3. The implementation is written in a less resource-restricted way, allowing for larger inputs without constraints on maximum values for the number of input lines, exception words, keywords, lengths of words, or lengths of input lines. The input words can be in upper or lower case, but exception words will still be lower-case and stored alphabetically. 

# Requirements
- Python 3
- Git

# File Structure

- 'concord4.py': Contains the main concordance class, named 'concord'.
- 'driver-original.py': Used at the command line. See 'Running the Program' below.
- 'driver-new.py': Accepts two file arguments, one for the name of the input file and one for the name of the output file. 

# Running the Program

## Using driver-orignal.py

To run the tenth test and compare it with the expected output, assuming all files are in the current directory: 

'''$ cat in10.txt | ./driver-original.py | diff - out10.txt'''

## Using driver-new.py

To create an ouput file, which you then must compare in a seperate command:

'''
$ ./driver-new.py --in in10.txt -- out \_out10.txt
$ diff out10.txt \_out10.txt
'''

Note: Make sure not to overwrite the correct test output file with your own output when using 'driver-new.py'

# Class Method

- The constructor for 'concord' takes two string parameters - the input file name, and the output file name. If the input filename is 'None', then input is to be obtained from stdin. If the output filename is 'None', output is not to be generated directly to the console
- The method named 'full_concordance' returns a list of strings corresponding to the output lines required.

