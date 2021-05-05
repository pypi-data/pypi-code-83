# -*- coding: utf-8 -*-
"""
there will not be any comments on stuff that should be self explanitory, or duplicates of
of previously explained lines.

credit to Brody Cooper
"""

import subprocess
subprocess.call('start /wait py -m pip install colorama', shell=True)
import colorama
colorama.init()

from random import choice
from random import randint as random
from AddQuestions import add_questions

def printstr(to_print):
  """

    this function prints each letter in string (to_print) in
    different random colors.
    returns none

    """
  string = ''
  for c in to_print:  # runs through string
    string += '\033[1;' + str(choice([31, 32, 34, 35, 36])) + 'm' + c  # adds each letter to final output with a color
  print(string, end='')  # prints colored string but dosent end line
  print('\033[1;0m' + '', end='')  # sets color to none

with open('symbols.txt', 'r') as file:
    symbols = file.read().split('|') # gets symbols and turns it into an array/list
originalsymbols = symbols  # stores original version of symbols for playing again
with open('elements.txt', 'r') as file:
    elements = file.read().split('|') # gets elements and turns it into an array/list
originalelements = elements  # stores original version of elements
correct = 0
wronganswers = []
wrongelements = list([])  # was having problems (edge cases) where original symbols wasnt working and this had similar code being applyed to it, need to do more testing
wrongsymbols = list([])


def confirm(string):
    """
    this function prints a string usig function printstr() and
    then waits for the user to press enter key to confirm.
    accepts a string as an argument to print.
    returns: input from user
    """
    printstr(string) # prints variable string in different colors
    a = input('') # waits for user to press enter
    return a

def main():
  """

  main function that the quiz is run from, excluding the summery.
  this function gives the option to add questions to the quiz, and says hello.
  if you have played before it says welcome back.

  """
  with open('historylog.txt', 'r') as file: # opens file history log in read mode
    accessed = file.read()
  if accessed == 'true': # checks if you have played before on current computer
    a = confirm('\nwelcome back! enter "add" to add questions, or just press enter to start...\n')
    if a == 'add':
      add_questions()
  else:
    with open('historylog.txt', 'w') as file:
      file.write('true') # if you havent played before it now says you have
    a = confirm('\nwelcome to my quiz! enter "add" to add questions, or just press enter to start...\n')
    if a == 'add':
      add_questions()
  for a in range(len(symbols)): # runs through questions in quiz
    askquestion(a) # calls function

def askquestion(q_num):
  """

  this is the function that the question is asked from, it accepts the paramater q_num, so it knows
  what question it is on.
  it then gets input and tests if input is the right answer and if wrong adds it to wronganswers
  list.

  """
  global correct, symbols, elements, wronganswers, wrongelements, wrongsymbols
  rand = random(0, len(symbols) - 1)
  questionnum = random(0, 1)
  question = [symbols[rand], elements[rand]]
  questiontype = ['symbol', 'name']
  printstr('\nquestion {0} of {1}'.format(q_num + 1, len(symbols) + len(wronganswers) + correct))
  printstr('\nwhat is the {0} of the element {1}?'.format(questiontype[1 - questionnum],question[questionnum]))
  if questiontype[1 - questionnum] == 'name':
      guess = input('').lower()
  else:
      guess = input('')
  if guess == question[1 - questionnum]:
    correct += 1
    printstr('Correct!\n')
  else:
    wronganswers.append('question {4}: what is the {0} of the element {1}?,  answer: {2}, your answer: {3}'.format(questiontype[1 - questionnum],question[questionnum],question[1 - questionnum],guess,q_num + 1, len(symbols) + len(wronganswers) + correct))
    wrongsymbols.append(question[0])
    wrongelements.append(question[1])
    printstr('Wrong! the answer was {0}, you put {1}!\n'.format(question[1 - questionnum],guess))
  symbols.pop(rand)
  elements.pop(rand)

def ender():
  """

  this function is run after all the questions have been answered,
  it basiclly prints a summery and asks if you want to play again, and if so it then asks if you want to
  play again only with questions you got wrong or all of them, and depending on this it
  resets symbols and elements lists

  """
  global correct, originalsymbols, wrongelements, wrongsymbols, originalelements, wronganswers, symbols, elements
  printstr('\nquiz summary:')
  if correct == len(symbols) + len(wronganswers) + correct:
    printstr('\nYou got all the questions correct!!! well done!')
  else:
    printstr('\n\nyour score: {0}/{1}'.format(correct, len(symbols) + len(wronganswers) + correct))
    printstr('\n\nquestions you got wrong:')
    for a in range(0, len(wronganswers)):
      printstr('\n' + str(wronganswers[a]).strip("['']"))
  while True:
      printstr('\n\ndo you want to go again? (y/n)')
      a = input('').lower()
      if a == 'y' or a == 'n':
          break
      else:
          printstr('\nplease write y or n')
  if a == 'n':
      printstr('\n\nbye!')
      raise SystemExit
  if a == 'y':
      if correct == len(symbols) + len(wronganswers) + correct:
          wronganswers = []
          correct = 0
          elements = tuple(originalelements)
          symbols = tuple(originalsymbols)
          wrongelements = []
          wrongsymbols = []
          return
      while True:
          printstr('\n\ndo you want to play only with questions you got wrong, or all of them? (wrong/all)')
          a = input('').lower()
          if a == 'wrong' or a == 'all':
              break
          else:
              printstr('\nplease write wrong or all')
      wronganswers = []
      correct = 0
      while True:
        if a == 'wrong':
          elements = list(wrongelements)
          symbols = list(wrongsymbols)
          wrongelements = []
          wrongsymbols = []
          return
        if a == 'all':
          elements = list(originalelements)
          symbols = list(originalsymbols)
          wrongelements = []
          wrongsymbols = []
          return
      return

while True:
    main()
    ender()
