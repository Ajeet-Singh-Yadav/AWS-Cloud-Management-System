from colorama import Fore, Style, init

init(autoreset=True)

def success(message):
    print(Fore.GREEN + message)

def error(message):
    print(Fore.RED + message)

def warning(message):
    print(Fore.YELLOW + message)

def info(message):
    print(Fore.CYAN + message)

def heading(message):
    print(Fore.MAGENTA + Style.BRIGHT + message)