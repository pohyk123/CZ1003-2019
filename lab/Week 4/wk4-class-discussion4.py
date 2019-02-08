# prints a pyramid of asterisks with user-input height
height = int(input('Please enter pattern width: '))

# prints ascending side of pyramid
for i in range(height+1):
    row = ''
    for j in range(i):
        row += '*'
    print(row)
    
# prints descending side of pyramid
for i in range(height-1,0,-1):
    row = ''
    for j in range(i):
        row += '*'
    print(row)