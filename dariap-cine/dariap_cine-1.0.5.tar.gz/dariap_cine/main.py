# coding: utf-8

import customer, movie
import random


def main():
    welcomemessage()


def welcomemessage():
    divider = '*=============================*'
    m_movieid = getrandommovie()

    seats = generateseats()

    print("\n".join([
        divider,
        "*   WELCOME TO ECAIB MOVIES   *",
        divider
    ]))
    print("        MOVIE OF THE DAY:   ")
    print(divider)
    print(movie.getinfo(m_movieid))
    print(divider)
    print("Looks like the guests are coming in... ")
    print(divider)
    assignseatstocustomers(m_movieid, seats)


def generateseats():
    seats = {}
    num_rows = 8
    num_cols = 9
    row = '8'

    for _ in reversed(range(num_rows)):
        column = 'A'
        for col in range(num_cols):
            seats[row + column] = False
            column = chr(ord(column) + 1)
        row = chr(ord(row) - 1)
    return seats


def getrandommovie():
    return random.randint(1, 12)


def getrandomseat():
    return random.choice('12345678') + random.choice('ABCDEFGHI')


def assignseatstocustomers(movid, seats):
    m_price = movie.getprice(movid)
    m_age = movie.getage(movid)
    for i in range(1, 15):
        c_age = customer.getage(i)
        c_money = customer.getmoney(i)
        customer.getinfo(i)
        if m_age > c_age:
            print("This customer isn't old enough!")
        elif m_price > c_money:
            print("This customer doesn't have enough money.")
        else:
            c_seat = getrandomseat()
            if seats[c_seat]:
                print(c_seat + " is occupied, let's find another.")
                new_seat = getrandomseat()
                print('Seat: ' + new_seat)
                seats[new_seat] = True
            else:
                print('Seat: ' + c_seat)
                seats[c_seat] = True
        print('-----------------------------')


if __name__ == "__main__":
    main()
