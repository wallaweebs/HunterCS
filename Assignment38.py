# CSci 127 Teaching Staff
# October 2017
# A program that uses functions to print out months.
# Modified by:  Debasree Sen
#Email: debasree.sen63@myhunter.cuny.edu

def monthString(monthNum):
    """
    Takes as input a number, monthNum, and
    returns the corresponding month name as a string.
    Example: monthString(1) returns "January".
    Assumes that input is an integer ranging from 1 to 12
    """

    monthString = ""
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    monthString += months[monthNum - 1]

    return(monthString)


def main():
    n = int(input('Enter the number of the month: '))
    mString = monthString(n)
    print('The month is', mString)


# Allow script to be run directly:
if __name__ == "__main__":
    main()
