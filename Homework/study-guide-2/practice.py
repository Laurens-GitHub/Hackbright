dic = {'soccer': 9, 'bravo': 8, 'whisky': ['tango', 'ginger', 'sour'],
'fantasy': False, 'jazz': ['cool', 'bossa nova', 'avant garde', 'Dixieland'],
'horoscope': ['gemini', 'pig', 'air']}

#add to a dictionary
dic['jingle'] = 'bells'

#change a value:
dic['horoscope'] = ['gemini', 'sheep', 'air']

#delete a key:
del dic['jazz']

#show a value:
dic['bravo']

# iterating over a dictionary

#this will print the keys
for item in dic:
    print(item)

#ALSO
for item in dic.keys():
    print(item)

#this will print the values:
for item in dic:
    print(dic[item])

#ALSO
for item in dic.values():
    print(item)

#This is how you print keys and values:
for key, value in dic.items():
    print(f'{key}: {value}')