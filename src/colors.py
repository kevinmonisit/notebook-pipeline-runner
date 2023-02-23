from datetime import datetime

PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'


def print_with_color(text, color, bold=False, childText: str = None):
    if(bold):
        print(BOLD + color + text + END, end=' ')
    else:
        print(color + text + color, end=' ')

    print(childText + " " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
