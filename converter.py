print("What do you want to convert: Type 1 for Meter and Type 2 for Centimeter")
user = int(input())

print("Enter a value you want to convert: ")
x=float(input())


def convertMToCm():
    converted = x*100
    print("Centimeter:", converted, "cm")


def convertCmToM():
    m = x / 100
    print("Meter:", m, "m")

if user == 1:
    convertMToCm()
elif user == 2:
    convertCmToM()
