import sys
try:
    with open(sys.argv[1], 'r') as f:
        contents = f.read()
        print(contents)
except (FileNotFoundError, IOError):
    print("plese enter the corret file name again:")