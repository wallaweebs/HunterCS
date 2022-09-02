#Name: Debasree Sen
#Email: debasree.sen63@myhunter.cuny.edu


line = input("Enter a non-empty string:")

while line == "":
    print("That was empty. Try again.")
    line = input("Enter a non-empty string:")
    if line != "":
        print("You entered:", line)