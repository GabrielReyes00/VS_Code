# Initialize Empty List
names_list = []

# Open Text File and Add Names to Empty List
with open("names.txt") as file:
    for line in file:
        names_list.append(line.rstrip())

# Sort New List Items and Print
for name in sorted(names_list):
    print(f"Hello, {name}")
