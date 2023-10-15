# Hybrid: multiple + single

class One:
    def __init__(self,name):
        self.name = name;

    def show(self):
        print(f"{self.name}");

class D1(One):
    def dance(self):
        print(f"Dancing d1");

class D2(One):
    def cook(self):
        print(f"Cooking d1");

class Two(D1,D2):
    def hide(self):
        print(f"{self.name} is hiding is name");

obj = Two("Two");
obj.show();
obj.dance();
obj.cook();
obj.hide();

# Hirerarchical: hierarchy

class manager:
    def __init__(self,name):
        self.name=name;

    def work(self,w):
        (self.work)=w;
        print(self.work);

class junior_1(manager):
    pass


class junior_2(manager):
    pass


class junior_3(manager):
    pass


j1=junior_1("J1");
j1.work("Cutting");

j2=junior_2("J2");
j2.work("Splicing");

j3=junior_3("J3");
j3.work("Merging");
