
def func():
    for i in [0,2,"string"]:
        try:
            division = 2/i
        except ZeroDivisionError:
            print("there is a zerodivision error")
        except TypeError:
            print("there is a type error")
        else:
            print(division)
        finally:
            print("Its always executed.")
func()
