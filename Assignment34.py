#Name: Debasree Sen
#Email: debasree.sen63@myhunter.cuny.edu

inpt = input("Please enter your list of names: ")

y = inpt.split(";")

print("You entered: ")

for names in y:
    z = names.split(", ")
    print(z[1], z[0])

print("Thank you for using my name organizer!")