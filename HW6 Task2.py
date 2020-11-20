#########1#########2#########3#########4#########5#########6#########7#########8
# Kevin R. Salger
# IS 640 Business Application Programming (Python)
#
#########1#########2#########3#########4#########5#########6#########7#########8
#        11111111112222222222333333333344444444445555555555666666666677777777778
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#########1#########2#########3#########4#########5#########6#########7#########8
"""
Homework 6, part 2
    Please use dictionary to keep the count of each letter.  Read a text file 
named "book.txt" that may have multiple lines.  Then create a "summary.txt" file 
that has the frequency of each letter, case-insensitive, i.e., the "a" and "A" 
are the same letter.  Each line has a record of the letter and frequency.  The 
last line should be a summary to tell if the file has all 26 letters.  A sample 
"summary.txt" is:
A 25
C 36
...
Y 2
Z 4
It doesn't have all letters.
    Another "book.txt" may generate the "summary.txt" as the following:
A 25
B 36
...
X 2
Y 1
Z 4
It has all letters.

"""

#########1#########2#########3#########4#########5#########6#########7#########8
# Global Variables
BookText = ''   # Record of the book file's text
alphabet = {}

#########1#########2#########3#########4#########5#########6#########7#########8
# Function(s)
#--------1---------2---------3---------4---------5---------6---------7---------8#
def change_case(bokstav):   # Swedish for "letter"
    """
    Changes case from lower to upper by converting to ascii, subtracting 32, and
    converting back to character
    """
    
    temp = ord(bokstav) - 32
    return chr(temp)
#--------1---------2---------3---------4---------5---------6---------7---------8#
#########1#########2#########3#########4#########5#########6#########7#########8
# Main
#  Read the book.txt file
try:
    with open('book.txt',mode='r') as BookText: # Open the text file book.txt
        for book_line in BookText:              # Reading line by line of text
            for each_char in book_line:         # Reading char by char of line
                ASCII_char = ord(each_char)     # Convert char to ASCII value
                if (ASCII_char == 13):          # Check for newline or Carriage Return
                    break                       # If CR detected, break out; new line
                elif ((ASCII_char >= 65) and    # If char in UPPERCASE range
                      (ASCII_char <= 90)):      # then
                      #find_ltr(each_char)       # either add to or update the dictionary
                     if each_char in alphabet:
                         alphabet[each_char] += 1
                     else:
                         alphabet[each_char] = 1
                elif ((ASCII_char >= 97) and    # If char in lowercase range
                      (ASCII_char <= 122)):     # then
                      capital = change_case(each_char)  # change the case of the letter, then
                      #find_ltr(capital)         # either add to or update the dictionary
                      if capital in alphabet:
                          alphabet[capital] += 1
                      else:
                          alphabet[capital] = 1
except:
    print('The file \'book.txt\' does not exist.')
    quit()  # Python threw an exception at this line.  Find solution.....

entry_count = 0
for entry in alphabet.items():
    entry_count += 1
if entry_count != 26:                               # If number of items != 26
    out_string = "It doesn\'t have all letters."    # then set out_string to alternate statement
elif entry_count == 26:                             # Don't need explicit check here, but inclusion
    out_string = "It has all letters."              # eases the reading of the code

with open('summary.txt', mode='w') as BookText:     # Open output file to write
    for letter, number in sorted(alphabet.items()): # Iterate through sorted dictionary entries 
        print(f'{letter} {number}',file=BookText)   # print key & value to file
        print(f'{letter} {number}')                 # print key & value to screen
    print(f'{out_string}',file=BookText)         # Print summary
    print(f'{out_string}')         # Print summary
    
# End Main
#########1#########2#########3#########4#########5#########6#########7#########8