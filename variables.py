# Variable starts with letter or underscore

myname = "swapna"
_mycountry = "India"
my_Native = "Tenali"

print(myname)
print(_mycountry)
print(my_Native)

# Variables do not start with numbers
# Variable is a case-sensitive
# Variable name is not any of the keyword


# To define multiword variable names we have different types of techniques like

# camel case  : Each word except first,remaining all starts with capital letter
myVariableName = "Fish"

# pascal case : Each word starts with capital letter
MyVariableName = "Chicken"

# snake case  : Each word seperated by an underscore character
my_variable_name = "Prawns"

print(myVariableName, MyVariableName, my_variable_name, sep='\n')

fruits = ["Apple","Papaya","strawberry"]
a,b,c = fruits
print(a,b,c,sep='\n')

x=5
y=10
z="manu"
print(x,y,z)

#Global Variable:
#---------------

p="swapna"
def myworld():
    print("Manoj"+p)
    
myworld()

p="India"
def myworld():
    global p
    p="country"
    print("Manoj"+p)

myworld()
print("Manoj"+p)



