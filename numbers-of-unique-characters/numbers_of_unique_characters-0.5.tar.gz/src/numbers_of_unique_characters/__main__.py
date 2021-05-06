from numbers_of_unique_characters.collection_framework import *

if __name__ == '__main__':
    args = add_args_argument()
    if args.file:
        print(get_number_of_unique_characters(args.file.read()))
    else:
        print(get_number_of_unique_characters(args.string))
