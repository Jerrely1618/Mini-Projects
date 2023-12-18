from tqdm import tqdm
import numpy as np
from time import sleep

def example1():
    LongList = np.zeros(100000000)
    
    for i in tqdm(LongList):
        pass

def example2():
    
    with tqdm(total=100) as pbar:
        for i in range(20):
            sleep(0.1)
            if i % 2 == 0:
                print(f"Processing user{i}")
                pbar.update(10)

if __name__ == "__main__":
    example1()
    # example2()







