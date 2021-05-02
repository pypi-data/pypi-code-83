class Accessor:

    @staticmethod
    def set(source, key, value):
        new_source = current = source
        levels = key.split('.')
        for index, level in enumerate(levels):
            if index + 1 == len(levels):
                current[level] = value
            else:
                if not level in current:
                    current[level] = {}

            current = current[level]

        return new_source

    @staticmethod
    def get(source, key):
        levels = key.split('.')
        value = source
        for level in levels:
            if level not in value:
                return None
            value = value[level]

        return value

    @staticmethod
    def has(source: dict, key):
        levels = key.split('.')
        value = source
        for level in levels:
            print(level in value)
            exit()
            if level not in value:
                return False

            value = value[level]

        return True

    @staticmethod
    def hasList(source: list, index):
        if index in source:
            return True

        return False
