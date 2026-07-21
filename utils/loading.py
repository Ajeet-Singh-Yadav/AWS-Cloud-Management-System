from tqdm import tqdm
import time


def progress_bar(task="Processing", seconds=2):

    print(f"\n{task}...\n")

    steps = 50

    delay = seconds / steps

    for _ in tqdm(range(steps), ncols=80):

        time.sleep(delay)