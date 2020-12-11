import sys

def fileReader(fileName):
    try:
        file = open(fileName, 'r')
        result = file.read()
        return result
    except:
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+++++           Error reading file          +++++")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")
        sys.exit(-1)