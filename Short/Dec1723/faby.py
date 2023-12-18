from colorama import init, Fore, Back, Style

init()
def example1():
    print(Fore.GREEN + Style.BRIGHT + "Waaasup" + Style.RESET_ALL)

def example2():
    print(Fore.RED + "NO NO Zone" + Style.RESET_ALL)
def example3():
    print(Back.CYAN + Fore.BLACK + Style.BRIGHT + "Fancy Text Example" + Style.RESET_ALL)
    print(Back.RED + Fore.YELLOW + Style.BRIGHT + "Welcome to the Colorful World!" + Style.RESET_ALL)
    print(Back.GREEN + Fore.MAGENTA + Style.BRIGHT + "This is a Mix of Colors and Styles!" + Style.RESET_ALL)
    print(Back.YELLOW + Fore.BLUE + Style.BRIGHT + "Feel the Rainbow! 🌈" + Style.RESET_ALL)
    print(Back.WHITE + Fore.BLACK + Style.BRIGHT + "Black on White" + Style.RESET_ALL)
    print(Back.RESET + Fore.RESET + Style.RESET_ALL + "Back to the default colors and styles.")
    

if __name__ == "__main__":
    example1()
    example2()
    example3()