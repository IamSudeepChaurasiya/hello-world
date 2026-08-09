def main():
    dollar=dollar_to_float(input("what was the amount of your meal?")) #format is $##.##
    percent=percent_to_float(input("what percentage would you like to tip?")) # format is ##%
    tip=dollar*percent
    print(f"Leave ${tip:2f}")

def dollar_to_float(a):
    pa=int(round(float(a.strip("$")),1))
    return pa

def percent_to_float(b):
    value=round(float(b.strip("%"))/100,2)
    return value

main()    