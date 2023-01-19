import json
from functools import reduce
class Components(object):
    def __init__(self,name,company):
        self.name = name
        self.company = company
    def display(self):
        print(self.name)
        print(self.company)
class Videocard(Components):
    def __init__(self,name,company,vram):
        self.vram = vram
        Components.__init__(self,name,company)
    def display(self):
        print(self.name)
        print(self.company)
        print(self.vram)
class Processor(Components):
    def __init__(self,name,company,Hz):
        self.Hz = Hz
        Components.__init__(self,name,company)
    def display(self):
        print(self.name)
        print(self.company)
        print(self.Hz)
    def __str__(self):
        return f'{self.name},{self.company},{self.Hz}'
class RAM(Components):
    def __init__(self,name,company,Gb):
        self.Gb = Gb
        Components.__init__(self,name,company)
    def display(self):
        print(self.name)
        print(self.company)
        print(self.Gb)
class Disk(Components):
    def __init__(self,name,company,Type,Gb):
        self.Type = Type
        self.Gb = Gb
        Components.__init__(self,name,company)
    def display(self):
        print(self.name)
        print(self.company)
        print(self.Type)
        print(self.Gb)
Processor1=Processor('Ryzen3600','AMD',4100)
Processor1.display()
print(list((Processor1.__str__())))
def Convert_To_string(first,second):
    return first + second
uppered_Processor =list(map(str.upper, (Processor1.__str__())))
print(uppered_Processor)
result = reduce(Convert_To_string,uppered_Processor)
print(result)

