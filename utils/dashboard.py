from datetime import datetime
from colorama import Fore

from config import REGION


def dashboard():

    now = datetime.now()

    print(Fore.YELLOW + "=" * 60)

    print(
        Fore.GREEN +
        f"Region : {REGION}"
    )

    print(
        Fore.GREEN +
        f"Date   : {now.strftime('%d-%b-%Y')}"
    )

    print(
        Fore.GREEN +
        f"Time   : {now.strftime('%I:%M:%S %p')}"
    )

    print(Fore.YELLOW + "=" * 60)