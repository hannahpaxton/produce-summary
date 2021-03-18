def summarize_delivery_logs(delivery_log):
    """Open the delivery log & print melon type, count, and amount"""

    #open the day 1 delivery log
    the_file = open(delivery_log)
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
    return 

print("Day 1")
summarize_delivery_logs("um-deliveries-20140519.txt")

print("Day 2")
summarize_delivery_logs("um-deliveries-20140520.txt")

print("Day 3")
summarize_delivery_logs("um-deliveries-20140521.txt")