# Write a function that takes in a string and returns a compressed version of that string. Your string will only contain non-numeric characters — that is, it will only contain letters, whitespace, and punctuation.

# 'Hello, world! Cows go moooo...' => 'Hel2o, world! Cows go mo4.3'

# 'balloonicorn' => 'bal2o2nicorn'



#define a function that takes in a string
def compressed_string(str):
    """replaces duplicate characters with numbers"""
    #split the string
    our_string = str.split()
    #iterate through the list of characters
    for char in range(0, len(our_string)):
        #establish a matching character count
        matching_char = 0
        #keep track of the current and previous characters.
        current_char = char
        #if the current and previous character match, increment a matching character count
        print(our_string)
        if current_char == our_string[char]:
            matching_char += 1
        #once there are no more matching charaters, remove duplicate characters from the list, equal to the value of matching character count -1.
        elif current_char != our_string[char]:
            our_string.pop(char)
        #insert the character count into the appropriate index
            our_string.insert(char, matching_char)
        #join the list on ''
        # print(our_string)
        # result = ''.join(our_string)
        # return the compressed string
        return(result)

print(compressed_string('balloonicorn'))