#print Day 1
print("Day 1")
#open the day 1 delivery log
the_file = open("um-deliveries-20140519.txt")
#iterate through the day 1 delivery log
for line in the_file:
    #strip the whitespace to the right of the line
    line = line.rstrip()
    #split the items in the line by the "|" character
    words = line.split('|')

    #select the first item in words
    melon = words[0]
    #select the first item in words, this will be changed to the 2nd
    count = words[1]
    #select the first item in words, this will be changed to the 3nd
    amount = words[2]

    #print statement passing through variables of count, melon, and amount
    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))

#closing of the file
the_file.close()


print("Day 2")
the_file = open("um-deliveries-20140520.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()


print("Day 3")
the_file = open("um-deliveries-20140521.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()
