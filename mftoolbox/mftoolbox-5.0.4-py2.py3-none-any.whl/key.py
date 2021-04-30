import uuid
import math
import random



class Erro(Exception):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message


class Key:

    def __init__(self, key = '', base_chave='', secret_4_digits = '1772'):
        if base_chave == '':
            raise Erro('Base para chave é mandatório')
        self.__base_chave = base_chave
        soma = 0
        for char in base_chave:
            soma += ord(char)
        self.__raiz_soma = math.floor(math.sqrt(soma))
        self.__secret_4_digits = secret_4_digits
        self.__key = key

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, var):
        self.__key = var

    @property
    def base_chave(self):
        return self.__base_chave

    @base_chave.setter
    def base_chave(self, var):
        self.__base_chave = var

    @property
    def secret_4_digits(self):
        return self.__secret_4_digits

    @secret_4_digits.setter
    def secret_4_digits(self, var):
        self.__secret_4_digits = var

    @property
    def raiz_soma(self):
        return self.__raiz_soma

    @raiz_soma.setter
    def raiz_soma(self, var):
        self.__raiz_soma = var

    def valida_chave(self):
        pass


    def verify(self):
        score = 0
        check_digit = self.key[5]
        check_digit_count = 0
        chunks = self.key.split('-')
        for chunk in chunks:
            if len(chunk) != 4:
                return False
            for char in chunk:
                if char == check_digit and chunk.count(char) == 1:
                    check_digit_count += 1
                score += ord(char)
        score_esperado = self.secret_4_digits +  self.raiz_soma
        if score == score_esperado and check_digit_count == 4:
            return True
        return False

    def generate(self):
        key = ''
        chunk = ''
        check_digit_count = 0
        tries = 0
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
        while True:
            while len(key) < 25:
                char = random.choice(alphabet)
                key += char
                chunk += char
                if len(chunk) == 4:
                    key += '-'
                    chunk = ''
            key = key[:-1]
            self.key = key
            if self.verify():
                return key
            else:
                tries +=1
                print(f'Testou chave {key} (tentativas = {tries})')
                key = ''

    def __str__(self):
        valid = 'Invalid'
        if self.verify(self):
            valid = 'Valid'
        return self.key + ':' + valid