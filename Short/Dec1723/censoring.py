from better_profanity import profanity
from icecream import ic

def example1():
    boss_msg = "Do you job! You p1ece of sHite."
    ic(profanity.censor(boss_msg))
    
def example2():
    custom_badwords = ['Hippopotomonstrosesquippedaliophobia', 'cat', 'little']
    profanity.load_censor_words(custom_badwords)
    ic(profanity.censor("My little cat has Hippopotomonstrosesquippedaliophobia."))
    
def example3():
    boss_msg = "Sorry about the prev message! Asshole."
    
    if profanity.contains_profanity(boss_msg):
        send_to_HR("He is not a very good boss", boss_msg)

def send_to_HR(msg: str, boss_msg: str)-> None:
    print("HR: We will take care of it.")
    del boss_msg
    
if __name__ == "__main__":
    example1()
    example3()