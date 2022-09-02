#Name: Debasree Sen
#Email: debasree.sen63@myhunter.cuny.edu

s = input(str("Enter a string: "))
ls = len(s)

for i in range(0,ls-1):
    print(s[0:i])

for i in range(0,ls-1):
    print(s[i:ls])

print("Your string is cool :)")
