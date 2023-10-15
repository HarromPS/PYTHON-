# Multilevel Inheritence: Derived from Derived classes

class Grandfather:
    def __init__(self,name,age):
        self.name = name;
        self.age = age;

    def walking(self):
        print(f"{self.name} is walking is garden");

class father(Grandfather):
    def job(self):
        print(f"{self.name} is doing a job");

class child(father):
    def playing(self):
        print(f"{self.name} is playing");

c1 = child("Amit",10);
c1.walking();
c1.job();
c1.playing()