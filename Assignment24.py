#Name: Debasree Sen
#Email: debasree.sen63@myhunter.cuny.edu

words = str(input("Enter nouns: "))

for x in words.split(" "):
    print("Number of words:" + len(x))
for c in words.split("s "):
    print("Fraction of your list that is plural is" + (x / len(c)))


