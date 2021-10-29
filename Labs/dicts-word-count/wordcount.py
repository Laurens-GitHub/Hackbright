"""Count words in file."""


# put your code here.

# define a function that accepts an input text file

# open the input file
# create an empty dictionary
# next, we will iterate through the input file
# define the line so that we can iterate through them
# define a delimiter of " "

# for each word in line, add the key into the dictionary
# at a value of 1

# if the word is found again, increment the value for the
#corresponding key

#bonus: account for commas and periods



#define the function

#use sys.argv to pass in a file
#import sys

def word_count(input_file):
    #open the input file
    input_file = open(input_file)

    #using sys.argv:
    #input_file = sys.argv[1]

    #create an empty dictionary
    word_dic = {}

    #iterate through the input file
    for line in input_file:
        #define a line
        line = line.rstrip()
        #bonus: account for punctuation
        line = line.replace(',', "")
        line = line.replace('.', "")
        line = line.replace('?', "")
        #define a word, delimited " "
        words = line.split(" ")
    # for each word in line, add the key into the dictionary
    # at a value of 1
        for word in words:
            word = word.lower()
            word_dic[word] = word_dic.get(word, 0) + 1
    return print(word_dic)

word_count('test.txt')