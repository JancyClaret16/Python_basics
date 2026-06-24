class School:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    def display(self):
        print('student name is',self.name,'age is',self.age,'city is',self.city)

class Enquiry(School):
    def __init__(self,name,age,city,fees,board):
        School.__init__(self,name,age,city)
        self.fees=fees
        self.board=board

class Admission(Enquiry):
    def display(self):
        print('student name is',self.name,'age is',self.age,'city is',self.city)
        print('fees will be around',self.fees,'selected board is',self.board)

s=School('Valan','7','chennai')
s.display()

a=Admission('Dylan','3','kum','50000','cbse')
a.display()
