
try:
    a = int(input("Please enter the number: "))
    if a <= 1000 or a>=9999:
        raise ValueError()
except ValueError:
    print("The length is too short/long !!! Please provide only four digits.")