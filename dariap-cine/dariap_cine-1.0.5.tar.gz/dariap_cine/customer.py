# coding=utf-8
import xml.etree.ElementTree as ET


class Customer:

    def __init__(self, name, money, age):
        self.name = name
        self.money = money
        self.age = age

    def getname(self):
        return self.name


tree = ET.parse('customers.xml')
root = tree.getroot()


def getinfo(custid):
    for guest in root.findall('.//customer[@id="' + str(custid) + '"]'):
        print('Name: ', guest.find('name').text)
        print('Money: ', guest.find('money').text)
        print('Age: ', guest.find('age').text)


def getmoney(custid):
    for guest in root.findall('.//customer[@id="' + str(custid) + '"]'):
        money = int(guest.find('money').text)
    return money


def getage(custid):
    for guest in root.findall('.//customer[@id="' + str(custid) + '"]'):
        age = int(guest.find('age').text)
    return age
