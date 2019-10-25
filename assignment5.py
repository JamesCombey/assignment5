'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
 The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
 The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
 After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

fileName = open('mbox-short.txt')
fileDict = dict()
for lines in fileName:
	lines = lines.rstrip()
	words = lines.split()
	if lines.startswith('From '):
		mail = words[1]
		fileDict[mail] = fileDict.get(mail,0) + 1

print('__'*30)
print('Dictionaries with Mail and count')
print('__'*30)
for mail,count in fileDict.items():
	print(mail, count)


bigMail = None
bigCount = 0

for mail,count in fileDict.items():
	if mail is None or count > bigCount:
		bigMail = mail
		bigCount = count
print('__'*30)
print('Big Mail with the largest count')
print('__'*30)
print(bigMail, bigCount)