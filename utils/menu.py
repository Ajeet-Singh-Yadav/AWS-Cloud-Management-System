from utils.banner import show_banner

from utils.dashboard import dashboard

from colorama import Fore

def main_menu():

    show_banner()

    dashboard()

    print(Fore.CYAN + """
╔═══════════════════════════════=════╗
║ 🖥️ 1 → Amazon EC2                  ║
║ 🪣 2 → Amazon S3                   ║
║ 🗄️ 3 → Amazon DynamoDB             ║
║ 🚪 4 → Exit                        ║
╚════════════════════════════════════╝
""")