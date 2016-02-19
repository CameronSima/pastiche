import glob
import os
import sqlite3
import re

from time import strftime
from collections import Counter
from random import randint

import formatting
import settings

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')

def parse_folder(subdirectory):
    files = glob.glob((STATIC_ROOT + '/' + subdirectory + '/*.txt'))
    result = []
    for f in files:
        if '\\' in f:
            title = f.split('\\')[-1]
        else:
            title = f.split('/')[-1]
        result.append(title.split('.')[0])
    return result

def get_poets():
    '''
    to add new poet checkboxes to the front end, simply
    add .txt files to static/corpus folder using the name
    of the author: (/static/corpus/poe.txt)
    '''
    return [poet.capitalize() for poet in parse_folder('corpus')]


'''
Return a dictionary from user selections
submitted by the HTTP post data
'''
def parse_data(formdata):
    choices = {}
    authors = []
    data = formdata.encode('utf-8').split('&')
    for element in data:
        prefix, value = element.split('=')
        if prefix == 'pf_Random':
            choices['random'] = True
        elif prefix[:2] == 'pf':
            choices['scheme'] = prefix[3:]
        elif prefix[:2] == 'nL':
            choices[prefix[3:]] = value
        else:
            authors.append(prefix)
    choices['authors'] = authors
    formatting.remove_duplicate_length(choices)
    print choices
    return choices


def write_combination_file(text, authors):
    filename = ''
    for author in authors:
        filename += author + '-' 
    filename = (STATIC_ROOT + '/compiled_texts/' 
                            + filename[:-1] + '.txt')
    with open(filename, 'w') as f:
        f.write(text)

def check_if_combo_exists(authors):
    files = parse_folder('compiled_texts')
    for file in files: 
        poets = file.split('-')
        if set(poets) == set(authors):
            return file
    return False

def build_mixed_corpus(authors):
    if not authors:
        return
    else:
        combined_text = ''
        for author in authors:
            fname = STATIC_ROOT + '/corpus/' + author + '.txt'
            for line in open(fname):
                combined_text += line
        return combined_text


def random_length():
    i = randint(2, 6)
    while i % 2 != 0:
        i = randint(2, 6)
    print i
    return i

def connect_to_db(name):
    conn = sqlite3.connect(name)
    return conn, conn.cursor()
    
def save_poem(poem):
    now = strftime("%m-%d-%Y")
    conn, c = connect_to_db(settings.DB)
    c.execute('''CREATE TABLE IF NOT EXISTS poems
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 date timestamp, 
                 poem text, 
                 likes INTEGER)''')

    c.execute('''INSERT INTO poems (poem, date, likes) 
               VALUES (?, ?, ?)''', (poem.encode('utf-8'), now, 0))
    conn.commit()
    conn.close()
    return c.lastrowid


def get_poems():
    conn, c = connect_to_db(settings.DB)
    c.execute("SELECT * FROM poems ORDER BY likes DESC")
    return c.fetchall()


def get_poem(id, cursor=False):
    if cursor:
        c = cursor
    else:
        conn, c = connect_to_db(settings.db)
    c.execute("SELECT * FROM poems WHERE id=?", id)
    return c.fetchone()

def return_likes(cursor, id):
    poem = get_poem(id, cursor)
    console.log(poem)

def vote(id, vote):
    '''vote will be a string equaling either -1 or 1.'''
    vote = int(vote)
    conn, c = connect_to_db(settings.DB)
    c.execute("UPDATE poems SET likes = likes + ? WHERE id=?", (vote, id))
    conn.commit()
    conn.close()
    
    


    



    
    


    
    
    
