import sys
from converter import Converter

convert = Converter()


def app():

    message = input('ENTER THE MESSAGE\n')
    program = input('SELECT PROGRAM\nE - phrase to morse code\nD - morse code to phrase\n')
    if program == 'E':
        convert.encode(message)
    elif program == 'D':
        convert.decode(message)
    else:
        sys.exit()


if __name__ == "__main__":
    app()