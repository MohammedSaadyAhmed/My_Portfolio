#create a function to get The leap year
def Check_leap(year):
#Checking Conditions for Leap year
    if (year % 4 ==0 ):
        if (year % 100 != 0 ) | (year % 400 == 0 ):
            print (" This year is a Leap year")
        else:
            print ("This year isn't a Leap year")
    else:
        print("This year isn't a Leap year")


#Input the year
year = int(input("Enter the year: "))
#Call The function
Check_leap(year)
