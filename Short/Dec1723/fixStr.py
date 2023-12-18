from ftfy import fix_text, explain_unicode,fix_encoding
from icecream import ic

def example1():
    ic(fix_text('âœ” No problems'))
    ic(fix_text('The Mona Lisa doesnÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t have eyebrows.'))
    
    
def example2():
    ic(fix_encoding("(à¸‡'âŒ£')à¸‡"))
    
def example3():
    ic(explain_unicode('(╯°□°)╯︵ ┻━┻'))
    
if __name__ == "__main__":
    example1()
    # example2()
    # example3()


