from icecream import ic

class exampleClass:
    name = "Joe Doe"
    age = 19
    def aging(self, num:int) -> int:
        self.age += num
        return self.age
def addtwo(numA:int, numB:int) -> int:
    return numA + numB

def iceex1():
    ex1 = "Hello World"
    ic(ex1)
def iceex2():
    ex2 = dict({"first_key":1,"second_key":2})
    ic(ex2)
def iceex3():
    ex3 = set([1,3,4,2])
    ic(ex3)
def iceex4():
    ic(addtwo(2,4))

if __name__ == "__main__":
    iceex4()