import openai

if __name__ == "__main__":
    def set_api_key(key):
        openai.api_key = key

    def get_version():
        return '0.0.1'

    def print_version():
        print('0.0.1')
