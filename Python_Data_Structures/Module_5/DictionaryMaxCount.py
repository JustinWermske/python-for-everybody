'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''
# get file name from user and open file
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# create a dictionary to count the number of times each sender appears in the file
counts = dict()
for line in handle:
    if not line.startswith("From:"):
        continue
    words = line.split()
    # get the sender's email address    
    email = words[1]
    # count the number of times the sender appears in the file
    counts[email] = counts.get(email, 0) + 1

# find the sender with the most messages
bigcount = None
bigword = None
for email, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = email
        bigcount = count

# print the sender with the most messages
print(bigword, bigcount)
