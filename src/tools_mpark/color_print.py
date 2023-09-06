class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def printc(*args, name='ENDC') -> None:
    print(getattr(bcolors, name) + str(args[0]), *args[1:], bcolors.ENDC)


if __name__ == '__main__':
    printc('Hello', 'world', name='HEADER')
