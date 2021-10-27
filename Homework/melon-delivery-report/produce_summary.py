print("Day 1")
the_file = open("um-deliveries-20140519.txt")
#opens the data file
for line in the_file:
#begins a for-loop
    line = line.rstrip()
#iterates through the data file, defining "line" as the individual strings
    data = line.split('|')
# defines '|' as a delimiter; break each line by the "|"
    melon = data[0]
# sets a melon value to the first position of each string
    count = data[1]
# sets count to the second position
    amount = data[2]
# sets amount to the third position
    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()
 

print("Day 2")
the_file = open("um-deliveries-20140520.txt")
for line in the_file:
    line = line.rstrip()
    data = line.split('|')

    melon = data[0]
    count = data[1]
    amount = data[2]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()


print("Day 3")
the_file = open("um-deliveries-20140521.txt")
for line in the_file:
    line = line.rstrip()
    data = line.split('|')

    melon = data[0]
    count = data[1]
    amount = data[2]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()
