file=open("jkfb.txt", "a")
while True:
        newItem= input("Enter new device: ")
        if newItem== 'exit':
            print("All done!")
            break

file.write(newItem + "\n")
file.close()
