def parseee():
    import argparse

    parser = argparse.ArgumentParser(description='PClone')
    parser.add_argument("--filename")

    args = parser.parse_args()

    with open(f'{args.filename}', 'rb') as file:
        bytess = file.read()

    with open(f'copy of {args.filename}', 'wb') as file_n:
        file_n.write(bytess)
