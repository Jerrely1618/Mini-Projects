import pyjokes

def example1():
    print(pyjokes.get_joke(language='en'))
    
def example2():
    print(pyjokes.get_joke(language='eu'))
    print(pyjokes.get_joke(language='es'))
    
def example3():
    print(pyjokes.pyjokes.all_jokes)
    
if __name__ == "__main__":
    example1()
    # example2()
    # example3()








