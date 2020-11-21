#########1#########2#########3#########4#########5#########6#########7#########8
# Kevin R. Salger
# IS 640 Business Application Programming (Python)
# 
#########1#########2#########3#########4#########5#########6#########7#########8
#        11111111112222222222333333333344444444445555555555666666666677777777778
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#########1#########2#########3#########4#########5#########6#########7#########8
"""
Homework 6, part 1
    This site https://www.whitehouse.gov/briefings-statements/remarks-president-trump-
state-union-address-3/ has the Remarks by President Trump in State of the Union
Address.  Please copy the text between "9:06 P.M. EST" to "10:24 P.M. EST" and
create a "summary.txt" file with the following statistics:
    - Total word count
    - Total character count
    - The average word length
    - The average sentence length
    - A word distribution of all words ending in "ly"
    - A list of top 10 longests words
    The file should be similar to -- the numbers are wrong, just for illustration:
    Total word count: 34093
    Total character count: 2030303
    The average word length: 7
    The average sentence length: 10

    A word distribution of all words ending in "ly"
    highly: 2
    totally: 1

    A list of top 10 longest words in descending order:
    Substantially, opportunities,...
    
    
"""
#########1#########2#########3#########4#########5#########6#########7#########8
# Imported Modules


#########1#########2#########3#########4#########5#########6#########7#########8
# Global Constants

#########1#########2#########3#########4#########5#########6#########7#########8
# Global Variables

#########1#########2#########3#########4#########5#########6#########7#########8
# Functions
"""
Remove punctuation?
"""
#--------1---------2---------3---------4---------5---------6---------7---------8#
#########1#########2#########3#########4#########5#########6#########7#########8
# Main
""" Read "remarks.txt"
    Increment word count 
    Increment char count
    Somehow use the dictionary to count all the word lengths & average them
    Average the sentence lengths.  How to determine sentence length?  By char or word? .?!
    Word distribution for "-ly" words
    List the 10 longest words
    Write "summary.txt"
    Close program
"""
#INPUT_FILE = 'towel.txt'
INPUT_FILE = 'remarks.txt' 
OUTPUT_FILE = 'summary.txt'

speech = {}     # Creating an empty dictionary
word = []
all_text = ''

# Read the file
try: 
    with open(INPUT_FILE,mode='r',encoding='utf-8') as full_text:  # full_text is a record
        for line in full_text: 
            word = line.split()
            for element in word:        # Entering words into dictionary "speech"
                all_text = all_text + element + ' '
                if element in speech:
                    speech[element] += 1   # If word exists in dictionary, increment count
                else:
                    speech[element] = 1    # If word is absent, add it in & increment count
                
    # Close file implicitly
except FileNotFoundError:                   # If the file doesn't exist, alert the user
    print('The file \'remarks.txt\' does not exist.') # and 
    quit()                                  # exit the program without executing remaining code


# Determine word count
word_count = 0      # Initialize word_count variable
words = []          # Create list called words
words = list(speech.values())   # Populate words
word_count = sum(words)         # Calculate sum of words

# Determine character count
char_count = 0
word_len_sum = 0
chars = []
                                
palabras = list(speech.keys())  # Create list of words called palabras
for entry in palabras:          # For each word in the list
    char_count += len(entry)    # Increment the count by the length of the entry
    char_count += 1             # Increment the count to account for a space after each entry
    word_len_sum += len(entry)  # For calc avg word length, next section
char_count -= 1                 # Subtract a space after end of text
# MS Word claims a character count of 733 without spaces, 896 with spaces, for "towel.txt"
# The above method only counts 719 with spaces.  Something isn't quite right.

# Average word length
mean_len = (word_len_sum)/(len(palabras)) 

# Average sentence length
    # Sentence length in words / number of sentence-ending punctuation
    # Search input text file for period (.), question (?), or exclamation (!) while counting words
sentence_count = 0  # number of sentences
sentence = []       # 
sent_len_sum = 0    # sentence length summary

for entry in all_text:
    if (entry == '.') or (entry == '?') or (entry == '!'):
        sentence_count += 1

sent_len_sum = len(palabras) / sentence_count
        
# Counting words ending in -ly
ly_dict = {}
ly_count = 0
for entry in palabras:
    if (entry.endswith('ly') or
        entry.endswith('ly.') or
        entry.endswith('ly?') or 
        entry.endswith('ly!') or
        entry.endswith('ly;') or
        entry.endswith('ly,') or
        entry.endswith('ly\'') or
        entry.endswith('ly\"')):
        ly_count += 1
        if entry in ly_dict:
            # increment count of dictionary entry
            ly_dict[entry] += 1
        else:
            # add entry to distribution dictionary
            ly_dict[entry] = 1
            
# The 10 longest words in descending order
from heapq import nlargest
ten_long = {}
large = []
for entry in palabras:
    ten_long[entry] = len(entry)    # create new dictionary with word:length of word
large = nlargest(10, ten_long, key = ten_long.get) 
#for val in large: 
#    print(val, ":", ten_long.get(val))

# Output
with open (OUTPUT_FILE,mode='a+') as output: 
    print(f'Total word count: {word_count}',file=output)
    print(f'Total char count: {char_count}',file=output)
    print(f'Average word length: {mean_len:.2f}',file=output)   
    print(f'Average sentence length (in words): {sent_len_sum:.2f}',file=output)
    print(f'Word distribution of words ending -ly:',file=output) #Needs better formatting
    for entrada,cuenta in ly_dict.items():
        print(f'{entrada}: {cuenta}',file=output)
    print(f'List of ten longest words:\n',file=output)  
    for val in large: 
        print(val, ":", ten_long.get(val),file=output)
# File closed implicitly because of indenting rules
# Screen output follows:  
print(f'Total word count: {word_count}')
print(f'Total char count: {char_count}')
print(f'Average word length: {mean_len:.2f}')   
print(f'Average sentence length (in words): {sent_len_sum:.2f}')
print(f'Word distribution of words ending -ly:') #Needs better formatting
for entrada,cuenta in ly_dict.items():
    print(f'{entrada}: {cuenta}')
print(f'List of ten longest words:\n')
for val in large: 
    print(val, ":", ten_long.get(val))
# End of Main 

