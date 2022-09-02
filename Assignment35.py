#Name: Debasree Sen
#Email: debasree.sen63@myhunter.cuny.edu

for i in range(3):
    hour = int(input("Enter hour (in 24 hour time): "))

    if hour < 12:
        print("Good Morning")
    elif 17 > hour >= 12:
        print("Good Afternoon")
    else:
        print("Good Evening")