import json
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
Processor1=Processor("Ryzen3600","AMD",4100)
Processor1.display()
f = open("lab_3.json", "w")
json.dump(Processor1.__dict__,f)
f.close()
f = open ('Lab_3.json', "r")
JsonObject = Processor(**json.loads(f.read()))
f.close()
JsonObject.display()
