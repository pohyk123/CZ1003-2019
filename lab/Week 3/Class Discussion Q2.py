boys_str = input('Enter the number of boys: ')
girls_str = input('Enter the number of girls: ')
boys_int = int(boys_str)
girls_int = int(girls_str)
students = boys_int + girls_int
boys_percent = format(boys_int/students,".0%")
girls_percent = format(girls_int/students,".0%")
print('Boys: {}'.format(boys_percent))
print('Girls: {}'.format(girls_percent))