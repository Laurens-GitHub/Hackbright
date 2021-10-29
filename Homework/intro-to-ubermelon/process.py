log_file = open("um-server-01.txt")
#defines a variable that opens the data file

def sales_reports(log_file):
    #creates a function that takes the data file as an argument
    for line in log_file:
        #iterate through the data file
        line = line.rstrip()
        #separate the data file by line
        day = line[0:3]
        # defines the day as the first 4 charaters on each line
        if day == "Mon":
            #establishes a condition
            print(line)
            #if the line begins with day, print the line


sales_reports(log_file)
#call the function, pass in the data file