from repairer import repair
def add_questions():
    """

    this function basiclly loops and asks you to add elements and their symbols until you write exit
    and then it ends the program.
    it adds the elements and symbols to the respective .txt file, saving them to that computer.

    """
    print('\ntype exit to quit')
    print('type restore to reinstall the original version of the quiz')
    while True:
        while True:
            element = input('what is the name of the element?').lower()
            if element == 'exit':
                print('\nbye!')
                raise SystemExit
            if element == 'restore':
                print('you will lose any elements you have added!')
                while True:
                    restore = input('continue? [y/n]')
                    if restore == 'y':
                        try:
                            repair()
                        except Exception:
                            print('Error: an error occured while trying to repair the program, please reinstall program')
                        break
                    if restore == 'n':
                        break
            if not element.isalpha():
                print('only letters, no special characters or numbers!')
                continue
            if len(element)<3:
                print('there are no elements with a name that short!')
                continue
            if len(element)>13:
                print('there are no element names that long!')
                continue
            break
        while True:
            symbol = input('what is the symbol for {0}?'.format(element)).lower()
            if not symbol.isalpha():
                print('only letters, no special characters or numbers!')
                continue
            if len(symbol)>2:
                print('there are no element symbols that long!')
                continue
            break
        symbol = symbol + '|'
        symbol = symbol[0].upper() + symbol[1]
        symbol.strip('|')
        with open('symbols.txt', 'a') as file:
            file.write('|'+symbol)
        with open('elements.txt', 'a') as file:
            file.write('|'+element)
        print('added!')