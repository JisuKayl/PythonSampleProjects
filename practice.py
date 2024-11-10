x = "Hello World!"
y = 100
pi = 22/7
list_sample = ["Do", "Re", "Mi", "Fa", "So", "La", "Ti", "Do2"]
dict_sample = {"Do":"100", "Re":"200", "Mi":"300", "Fa":"400", "So":"500", "La":"600", "Ti":"700", "Do2":"800"}

#print sample
"""print(x)
print(type(y))

print("This value of x is " + str(y))
z = str(y)
print(type(z))"""
#converting to float
"""print("{:.3f}".format(pi))"""

#Lists sample
"""print(type(list_sample))
print(len(list_sample))
print(list_sample)"""

#Lists handling
"""print(list_sample[-1])
list_sample[5] = "WOW"
del list_sample[1]
print(list_sample)"""

#Dictionary
"""print(type(dict_sample))
print(dict_sample)
print(dict_sample["Do"])
dict_sample["Do2"]="1000"
print(dict_sample["Do2"])
a = "Mi" in dict_sample
print("Mi" in dict_sample)
print(a)"""

#input() function
""""firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
location = input("What is your location? ")
age = input("What is your age? ")
print("Hello " + firstName + " " + lastName + "! ")
print("Pupuntahan kita dyan sa: " + location + ". ")

if(type(age) == int):
    print(age + " y.o. ka na pala, tanda mo na.")
else:
    print("MALI KA NAMAN BEH")"""

#loop
"""n = 1
while(n!=100):
    print("WOW")
    n=n+1"""

#Create a python script that will ask user for 2 numbers. The script will print the sum, difference, product, and quotient.
n1 = input ("Input first number: ")
n2 = input ("Input second number: ")

"""number1 = int(n1)
number2 = int(n2)

sum_int = number1 + number2
difference_int = number1 - number2
product_int = number1 * number2
quotient_int = number1 / number2

sum_str = str(summ)
difference_str = str(difference)
product_str = str(product)
quotient_str = str(quotient)

print("The sum of " + n1 + " and " + n2 + " is: " + sum_str)
print("The difference of " + n1 + " and " + n2 + " is: " + difference_str)
print("The product of " + n1 + " and " + n2 + " is: " + product_str)
print("The quotient of " + n1 + " and " + n2 + " is: " + quotient_str)"""

if((n1.isnumeric() == True) and (n2.isnumeric() == True)):
    print("The sum of " + n1 + " and " + n2 + " is: " + str(int(n1)+int(n2)))
    print("The difference of " + n1 + " and " + n2 + " is: " + str(int(n1)-int(n2)))
    print("The product of " + n1 + " and " + n2 + " is: " + str(int(n1)*int(n2)))
    print("The quotient of " + n1 + " and " + n2 + " is: " + str(int(n1)/int(n2)))
else:
    print("Error")
