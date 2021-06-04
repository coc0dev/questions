# Question 1
def hello_name(username):
    """print hello + username"""
    print("Hello! " + username.title())

hello_name('evan')

# Question 2
for num in range(1,100): # Print all odd numbers between 1 and 100
    if num % 2 == 1:
        print(num)

# Question 3
def max_num_in_list(list):
    """return max number of items in a list"""
    max = list[0]
    for a in list:
        if a > max:
            max = a
    print("\n" + str(max) + " is the largest number in the list")

max_num_in_list([10, 20, 30, 40, 50, 60])

# Question 4
def is_leap_year(year):
    """finds if a year is a leap year"""
    if year % 4 == 0:
        print("\nTrue, " + str(year) + " is a leap year")
    elif year % 400 == 0:
        print("\nTrue, " + str(year) + " is a leap year")
    else: 
        year % 100 == 0
        print("\nFalse, " + str(year) + " is not a leap year")

is_leap_year(2000)
is_leap_year(2001)
is_leap_year(2020)

# Question 5
def is_consecutive(*a_list):
    print("\n" + str(True if sorted(a_list) == list(range(min(a_list), max(a_list)+1)) else False))

is_consecutive(1, 2, 3, 4, 5)
is_consecutive(1, 2, 4, 5, 6)