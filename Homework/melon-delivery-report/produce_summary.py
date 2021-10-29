print("Day 1")
the_file = open("um-deliveries-20140519.txt")
#defines a variable that opens the data file
for line in the_file:
    #iterates through the data file
    line = line.rstrip()
    #separates the lines by line break
    words = line.split('|')
    #delimits the line by a bar
    melon = words[0]
    #defines "melon" as the first item in the line
    count = words[1]
    #defines "count" as the second item in the line
    amount = words[2]
    #defines "amount" as the third item in the line
    print(f"Delivered {count} {melon}s for total of ${amount}")
    #prints the produce summary
the_file.close()
#closes the data file

print("Day 2")
the_file = open("um-deliveries-20140520.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()


print("Day 3")
the_file = open("um-deliveries-20140521.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()
