import sys
import re

from sources.printErrorMsg import printErrorMsg

class MixValidation:

    def __init__(self, bufferReader):
        self.bufferReader = bufferReader
    
    def run(self):
        self.mixSymbolValidation()
        self.mixCharValidation()
        self.mixArgValidation()
        self.inputValidtion()
    
    def mixSymbolValidation(self):
        string = self.bufferReader.split(" ")
        for x in string:
            match = re.search(r'[^FBRLUD2\']', x)
            if (match):
                printErrorMsg("Please only enter valid symbols: F B R L U D 2 \'")
    
    def mixCharValidation(self):
        string = self.bufferReader.split(" ")
        for x in string:
            match = re.search(r'[A-Z]+', x)
            if (match == None):
                printErrorMsg("There must be atleast one valid character entered: F B R L U D")
    
    def inputValidtion(self):
        string = self.bufferReader.split(" ")
        for x in string:
            if (len(x) == 0):
                printErrorMsg("Invalid space")
            if (len(x) > 2):
                printErrorMsg("Extra invalid symbol(s)")
    
    def mixArgValidation(self):
        string = self.bufferReader.split("\n")
        if (len(string) != 1):
            printErrorMsg("Only one argument is allowed")