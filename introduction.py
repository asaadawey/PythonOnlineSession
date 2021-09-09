from datetime import date
#Defining variables

my_age = 21;
my_name = "Ahmed";

# If statements

if my_age > 18:
    print('You have exceed the legal age')
else:
    print('You haven\'t exceed the legal age')

# and / or
if my_age > 18 and my_name == "Ahmed":
    print('Authenticated')
#Functions and imports

def get_year(age):
    todays_date = date.today();
    return todays_date.year - age;

print(get_year(21));

#Arrays

my_favourite_fruits = ["Banana" , "Apple" , "Grapes"]


# For and while loops

for fruit in my_favourite_fruits:
    print(fruit);

# Traditional For ( int i = 0) loop
for i in range(10):
    print(i);

# while
i = 1;
while i < 6:
    print(i);
    i+=1;
    
#conversions
#from string to int and vice versa

my_string_age = str(my_age);
int_age = int(my_string_age);

#Useful keyboard shortcut

# Ctrl + Arrows - Go up and down
# Shift + Arrows - Go up and down with
# Refactor F2 
# Ctrl + Click Multiple selection
# Ctrl + D Multiple auto selection
# Shift + Alt + Down / Up Code duplication
# Ctrl + P Code search
# Ctrl + P + @ Functions and symbols search
