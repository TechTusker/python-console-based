class record():
    def __init__(self):
        print("Press 1 to add new student")
        print("press 2 edit existing student")
        print("press 3 to display all information")
        print("press 4 to exit program")
        self.operator=0
    def getdata(self):
        self.operator=int(input("Enter choice-"))
    def setdata(self):
        self.roll=[]
        self.name=[]
        self.age=[]
        self.city=[]
        if(self.operator==1):
            self.r=int(input("Enter unique identifier"))
            for i in self.roll:
                if(self.r==self.roll[i]):
                    print("student already exists")
                else:
                    self.n=input("Enter new student's name")
                    self.c=input("Enter new student's city")
                    self.a=int(input("Enter new student's age"))
                    name.append(self.n)
                    age.append(self.a)
                    city.append(self.c)
                    roll.append(self.r)
        if(self.operator==3):
            print(self.name)
            print(self.roll)
            print(self.age)
            print(self.city)
t=record()
t.getdata()
t.setdata()
        
