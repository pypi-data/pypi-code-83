import configparser


class ConfigParserManager:

    @staticmethod
    def read(file_name, section=''):
        try:
            config = configparser.ConfigParser()
            config.read(file_name)
            if section != '':
                return dict(config[section])

            return config
        except:
            return ''

    def update(self, file_name, value, section='user'):
        config = configparser.ConfigParser()
        config = self.read(file_name)

        config[section] = value

        with open(file_name, 'w') as f:
            config.write(f)
