#if practice 1
"""nativeVLAN = 1
dataVLAN = 100
if nativeVLAN == dataVLAN:
    print("The native VLAN and the data VLAN are the same")
else:
    print("The native VLAN and the data VLAN are different")"""

#if practice 2
"""n1 = input("pls: ")
n2 = input("again: ")

if (n1 > n2):
    print (n1)
elif (n2 == n1):
    print ("equal")
else:
    print(n2)"""

#if practice 3
"""number = int(input("dito: "))

if (number%2 == 0):
    print("Even")
else:
    print("Odd")

if (number > 0):
    print("pusitib")
elif(number == 0):
    print("sirow")
else:
    print("nega")"""

#if practice 4
"""aclNum = int(input("What is the IPv4 ACL number? "))
if aclNum >= 1 and aclNum <=99:
    print("standard IPv4 ACL")
elif aclNum >= 100 and aclNum <=199:
    print("extended IPv4 ACL")
else:
    print("HINDE")"""

#Write a python script that will input a score from 1 to 10 and will print the equivalent letter score
"""n = 1

while(n!=0):
    score_input = input("Input score from 1 to 10: ")
    if (score_input.isnumeric() == True):
        score = int(score_input)
        if (score>= 1 and score<=10):
            if (score == 10 or score == 9):
                print("A")
            elif (score == 8):
                print("B")
            elif (score == 7):
                print("C")
            elif (score == 6):
                print("D")
            else:
                print("F")
            break
        else:
            print("Nasa labas ka naman eh")
    else:
        print("Enter a number pls.")"""

#for loop
"""device = ["Lolo mo", "Lolo ko", "Lola mo", "Lola ko"]
switches = []
for item in device:
    if "Lola" in item:
        switches.append(item)
for item in device:
    if "Lolo" in item:
        print(item)
        
print(switches)"""

#while loop sample 1
"""x = input("Ples: ")
y = 1
while True:
    if (x == "q" or x == "quit"):
        break
    x = int(x)
    print(y)
    y=y+1
    if y>x:
        break"""

#alternative  counting
"""in_no = int(input("Enter Number"))
for x in range(in_no):
    print(x+1)"""

#external file
"""file = open("bahaykubolyrics.txt", "r")
store = []
for x in file:
    x = x.strip()
    store.append(x)

file.close()

print(store)

for y in store:
    print(y)"""

#activity

while True:
    buksan = open("boom.txt", "a")

    lagay = input("New device: ")

    if lagay == "exit":
        print("Paalam")
        break

    else:
        buksan.write("\n" + lagay)
        buksan.close()

while True:
    buksan = open("boom.txt", "r")
    yn = input("Print? Enter 'Yes' or 'No': ")
    
    if (yn == "Yes"):
        print(buksan.read())
    elif (yn == "No"):
        break
        buksan.close()
    else:
        print("Mali ka naman!??!")


    
