# User Input to Ask for Names
name = input("Please provide a name(s) to add into our file: ")

# Use "Open" to Make Filename and "a" to Append to File 
with open("names.txt", "a") as file:
    # Use "Write" to add into file
    file.write(f"{name}\n")


# Use "Open" and "r" to Read Text from File 
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines: 
    # Using "end = " because write function above has a \n at end of name. Could use line.rstrip() to remove \n at end names string from above function before printing (which has \n by default) 
    print("hello, ", line, end = "")

#######################################################

# Improved Version of Code from Above
with open("names.txt", "r") as file:
    for line in file:
        print("Hello, ", line.rstrip())

########################################################




