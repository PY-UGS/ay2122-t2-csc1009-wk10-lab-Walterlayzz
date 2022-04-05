mods = {
    "CSC1006":"Mathematics 2",
    "CSC1007":"Operating Systems",
    "CSC1008":"Data Structure and Algorithm",
    "CSC1009":"Object-Oriented Programming",
    "CSC1010":"Computer Networks"
}

module = input("Enter a module code: ")
print(mods.get(module.upper()))

print("\n")
for i in range(102,26, -1):
    if(i%2==1):
        print("Value of x is : ", i)
