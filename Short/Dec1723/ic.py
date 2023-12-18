from icecream import ic

def example1():
    ex1 = "Hello World"
    ic(ex1)
    
def example2():
    ex2 = dict({"first_key":1,"second_key":2})
    ic(ex2)
    
def example3():
    ex3 = set([1,3,4,2])
    ic(ex3)
    
def addtwo(numA:int, numB:int) -> int:
        ic()
        return numA + numB
def example4():
    ic(addtwo(2,4))

if __name__ == "__main__":
    example1()
    example2()
    example3()
    example4()