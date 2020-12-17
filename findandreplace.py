"""This is a program to find and replace a given word in a text file"""
filename=input('Enter filename: ')#filename
fword=input('word to find: ')#word to find
sword=input('word to replace: ')#word to replace
changed=0
reallines=[]
with open(filename,'r') as fileobject:
	contents=fileobject.readlines()
	for line in contents:
		if line.count(fword) != 0:
			changed+=1
			line=line.split(fword)
			line=sword.join(line)
			reallines.append(line)
		else:
			reallines.append(line)
if changed != 0:
	with open('demo.txt','w') as fileobject:
		for line in reallines:
			fileobject.writelines(line)
elif changed==0:
	print('No such word exist')
print('Number of changes made: ',changed)
