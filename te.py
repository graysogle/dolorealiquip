from colorama import Fore, Back, Style

def cprint(text, color):
    """Prints text in a specified color."""
    color_dict = {
        "black": Fore.BLACK,
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
    }
    print(color_dict[color] + text + Style.RESET_ALL)

user = ["John", "Doe"]
cprint(f'{user[0]:<4}cleaned', 'cyan')
