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


def printc(*args, name: str = 'ENDC', **kwargs) -> None:
    '''HEADER, OKBLUE, OKCYAN, OKGREEN, WARNING, FAIL, ENDC, BOLD, UNDERLINE'''
    if len(args) == 1:
        print(getattr(bcolors, name.upper()) + str(args[0]) + bcolors.ENDC, **kwargs)
    else:
        print(getattr(bcolors, name.upper()) + str(args[0]), *args[1:-1], args[-1] + bcolors.ENDC, **kwargs)


if __name__ == '__main__':
    # get all attributes of bcolors
    for attr in dir(bcolors):
        if attr.isupper():
            printc(attr, name=attr, end=' ')
