# a sentence to be split into a list
letters = 'I make alot of money'
# then we use the .split to separate the words into a list
x = letters.split()
# letters will be split as per the spaces into a list
print(x)

# now to open my file 'mbox-short.txt'
handle = open('mbox-short.txt')
email = dict()
names_list = []
# then to loop through the line
for line in handle:
    # this strips the new line space on the lines of the document
    line = line.lstrip()
    # this splits the lines of the document into lists
    wds = line.split()
    # this if block deals with any blank spaces by skipping them
    if len(wds) < 1:
        # print("ignored")
        continue
    # this if block looks at the first word of each list created to see if it starts with from
    if wds[0] == "From":
        # this helps me isolate the email addresses in the file and when the emails were sent
        # print(wds[1], wds[2])
        # names helps isolate the names on the email addresses
        names = wds[1].split("@")
        names_list.append(names[0])
print(names_list)

# now to create a dictionary and add on to it
for e in names_list:
    email[e] = email.get(e, 0) + 1
print(email)

# then we search for the person who has sent the most emails
sent = -1
person = None
# this for loop reads through all the items and compares them to find who sent the most emails
for k, v in email.items():
    if v > sent:
        sent = v
        person = k
print(person, sent)


