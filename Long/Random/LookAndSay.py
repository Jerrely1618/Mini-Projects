from time import sleep

class Look():
    def __init__(self,initial) -> None:
        self.sequence = initial
    
    def run(self,n):
        print(self.sequence)
        for i in range(int(n)):
            cnt = 0
            newSequence = ""
            lastDigit = self.sequence[0]
            for digit in self.sequence:
                if digit != lastDigit:
                    newSequence += str(cnt) + lastDigit
                    cnt = 1
                else:
                    cnt += 1
                lastDigit = digit
            newSequence += str(cnt) + lastDigit
            
            self.sequence = newSequence
            print(self.sequence)
            
if __name__ == '__main__':
    initialSequence = input("Enter initial sequence: ")
    say = Look(initialSequence)
    repeat = int(input("Enter repetitions #: "))
    say.run(repeat)