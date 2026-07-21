import pyfiglet
from colorama import Fore, Style

def show_banner():

    banner = pyfiglet.figlet_format(
        "AWS Cloud",
        font="slant"
    )

    print(Fore.CYAN + Style.BRIGHT + banner)