import ssl
import nltk
import random
from flask import Flask, render_template
import pickle
from termcolor import colored
from tqdm import tqdm
import threading
import json
import sys
special_characters = '~!@#$%^&*()-_=+[{]}\|;:\'",<.>/?'
stng = "Hi. My name is bob'. How are you?"
def clean_up(character,string):
    stuff = string
    while stuff.find(character)!=-1:
        print(character)
        print(stuff.find(character))


        stuff = stuff.replace(character,'')
    return stuff.lower()
'''
for item in list(special_characters):

    stng =clean_up(item,stng)
'''
def finish(directory):
    stng = open(directory).read()
    for item in list(special_characters):
        stng = clean_up(item, stng)
    return nltk.word_tokenize(stng)
'''
big_data = finish('train.txt')
thingy = open('data.pickle','wb')
pickle.dump(big_data,thingy)
thingy.close()
'''
bugaloo = 'cool'
numaloo = 0
def turn_to_model(wordtokenization):
    global bugaloo, numaloo
    big_json_file = {}
    word_tokenization = wordtokenization
    for item in tqdm(word_tokenization):

        if word_tokenization.index(item) != len(word_tokenization)-1:
            if item in [key for key in big_json_file]:
                pass
            else:
                big_json_file[item] = {}
            if word_tokenization[word_tokenization.index(item)+1] in [key for key in big_json_file[item]]:
                pass
            else:
                big_json_file[item][word_tokenization[word_tokenization.index(item)+1]] =0
            big_json_file[item][word_tokenization[word_tokenization.index(item) + 1]]+=1
        numx = 1
        word_tokenization = word_tokenization[numx:]
        numx += 1

        bugaloo = item

        numaloo +=1





    return big_json_file


def stuffs():
    global big_data_pool
    big_data_pool = pickle.load(open('data.pickle','rb'))
    coolz = turn_to_model(big_data_pool)

    json.dump(coolz,open('modelo.json','w'))
    print(colored("NOOOOOOOO",'green'))
    print(colored("NOOOOOOOO", 'green'))
    print(colored("NOOOOOOOO", 'green'))

    sys.exit('SOTP')
def save(dictionary,name):
    json.dump(dictionary, open(name, 'w'))
def load(directory):
    return json.load(open(directory,'r'))

'''
app = Flask(__name__)
@app.route('/')
def index():
    global numaloo
    global bugaloo
    global big_data_pool
    threading.Thread(target=stuffs,daemon=True).start()
    while True:
        return render_template('index.html',big_word=bugaloo,num=numaloo,noice_num=len(big_data_pool))
@app.route('/sotp')
def second():
    global numaloo
    global bugaloo
    global big_data_pool

    for x in range(2):

        return render_template('index.html', big_word=bugaloo, num=numaloo, noice_num=len(big_data_pool))
app.run()

'''
#cloo = turn_to_model(['my','name','is','john'])
#things = ['my','name']
def generation(things,cloo,prog = False):
    global cool
    while True:
        if things[-1] in [key for key in cloo]:
            words = [key for key in cloo[things[-1]]]

            nums = []
            for item in words:
                nums.append(cloo[things[-1]][item])
            next_word = random.choices(words,nums)
            things.append(next_word[0])
        else:
            break
        oof = ' '
        if prog:
            print(oof.join(things))
        cool = oof.join(things)
    return oof.join(things)
#mlode = json.load(open('modelo.json','r'))
#generation(things=things,cloo=mlode)
