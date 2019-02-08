# This script aims to count the number of strings with letter 'a' and ends the program with an input '####'.

#initialise count to zero
count = 0

# receives input and adds an increment to the counter for each contianing with 'a'
while True:
	string 	= input("Enter a string (enter #### to stop): ")
	if(string == '####'): break
	for l in string:
		if(l=='a'):
			count+=1
			break
	print(str(count),"strings with letter 'a'")