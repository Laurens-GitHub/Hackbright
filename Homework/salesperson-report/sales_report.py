"""Generate sales report showing total melons each salesperson sold."""


#not snake case: salespeople = []
sales_people = [] #establishes an empty list for salespeople
melons_sold = []  #establishes an empty list for melons sold

# bad naming convention: f = open('sales-report.txt')

data_file = open('sales-report.txt') #defines a variable that opens the data file
# needs "for thing in things" convention: for line in f:
for line in data_file: #iterates throught the data file
    line = line.rstrip() #separates our data by line breaks, assigns to variable
    entries = line.split('|') #delimits the lines by '|'

    # should be snake case: salesperson = entries[0]
    sales_person = entries[0]
    melons = int(entries[2])
    #global translate "salespe*" to "sales_pe*"
    if sales_person in sales_people: #establishes a condition. if the name is already found in the list "sales_people"
        position = sales_people.index(sales_person) #then set the "position" to the index of this person's name in "sales_people" list

        melons_sold[position] += melons #and increment the melon sales associated with that person.
    else: #if not
        sales_people.append(sales_person) #add this person the the list
        melons_sold.append(melons) #append their associated melon sales to melons list


#change i to number: for i in range(len(salespeople)):
for number in range(len(sales_people)):
    print(f'{sales_people[number]} sold {melons_sold[number]} melons')