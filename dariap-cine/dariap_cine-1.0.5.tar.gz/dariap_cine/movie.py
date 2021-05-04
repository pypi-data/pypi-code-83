# coding=utf-8

import xml.etree.ElementTree as ET


class Movie:

    def __init__(self, director, title, genre, price, age, duration, description):
        self.director = director
        self.author = director
        self.title = title
        self.genre = genre
        self.price = price
        self.age = age
        self.duration = duration
        self.description = description

    def getdirector(self):
        return self.director

    def gettitle(self):
        return self.title

    def getgenre(self):
        return self.genre

    def getduration(self):
        return self.duration

    def getdescription(self):
        return self.description


tree = ET.parse('movies.xml')
root = tree.getroot()


def getinfo(movieid):
    for movie in root.findall('.//movie[@id="' + str(movieid) + '"]'):
        print('Director: ', movie.find('director').text)
        print('Title: ', movie.find('title').text)
        print('Genre: ', movie.find('genre').text)
        print('Price: ', movie.find('price').text)
        print('Age: ', movie.find('age').text)
        print('Duration: ', movie.find('duration').text)
        print('Description: ', movie.find('description').text)


def getprice(movieid):
    for movie in root.findall('.//movie[@id="' + str(movieid) + '"]'):
        price = int(movie.find('price').text)
    return price


def getage(movieid):
    for movie in root.findall('.//movie[@id="' + str(movieid) + '"]'):
        age = int(movie.find('age').text)
    return age
