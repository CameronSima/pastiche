import random
import time
import datetime
import os
import numbers
from random import randint

DEBUG = False

import utilities
import rhymer
import settings
import formatting

class Markov(object):
    def __init__(self, open_file):
        self.cache = {}
        self.words = open_file.split()
        self.word_size = len(self.words)
        self.database()

    def triples(self):
        """ Generates triples from the given data string. So if our string were
                "What a lovely day", we'd generate (What, a, lovely) and then
                (a, lovely, day).
        """
        if len(self.words) < 3:
            return
        
        for i in range(len(self.words) - 2):
            yield (self.words[i], self.words[i+1], self.words[i+2])
            
    def database(self):
        for w1, w2, w3 in self.triples():
            key = (w1, w2)
            if key in self.cache:
                self.cache[key].append(w3)
            else:
                self.cache[key] = [w3]
                
    def generate_markov_text(self, size=30):
        seed = random.randint(0, self.word_size-3)
        seed_word, next_word = self.words[seed], self.words[seed+1]
        w1, w2 = seed_word, next_word
        gen_words = []

        for i in xrange(size):
            gen_words.append(w1)
            
            w1, w2 = w2, random.choice(self.cache[(w1, w2)])
        gen_words.append(w2)
        self.text = ' '.join(gen_words)
        return self.text

    def format_poem(self):
        # period = False
        puntc = ['.', '?', '!']
        puncts = [',', '-', ';', ':']
        illegal = ['{', '}', '"', '[', ']', '_', ')', '(', '/']
        illegal_words = ['the', 'The', 'and']
    
        # End the poem on the nearest punctuation mark. 
        # If the poem contains none, add a period to the end.
        # for x in reversed(range(len(self.text))):
        #     if self.text[x] in puntc:
        #         self.text = self.text[:x+1]
        #         period = True
        #         break
        # if not period and len(self.text.split(' ')) != 2:
        #     self.text = self.text + '.'

        new_poem = ''
        try:
            for x in range(len(self.text)):

                if x == 0:
                    new_poem += self.text[x].upper()


                # Remove bad characters and numbers
                elif self.text[x] in illegal or isinstance(self.text[x], numbers.Number):
                    pass

                # Capitalize all i pronouns.
                elif len(self.text) > x > 0 and self.text[x-1] == ' ' and self.text[x+1] == ' ' and self.text[x] == 'i':
                    new_poem += self.text[x].upper()
                    

                # Capitalize beginning of new sentences.
                elif len(self.text) > x > 0 and self.text[x-2] in puntc and self.text[x-1] == ' ':
                    new_poem += self.text[x].upper()

                else:
                    new_poem += self.text[x]

            if new_poem.split()[:-1] in illegal_words:
                new = new_poem.split()
                new_poem = new[:-1]

            # Don't end a poem on incorrect punctuation.
            if new_poem[:-1] in puncts:
                
                new_poem = new_poem[:-1]
            if new_poem[:-1] not in puntc:
                new_poem += random.choice(puntc)

            self.text = new_poem
        except:
            self.text = "Sorry...There was an error. Please try again!"

'''
This subclass uses a generator instead of opening
the files in memory. However, it runs nearly 3x 
more slowly.
'''
class MarkovGenerator(Markov):
    def __init__(self, authors):
        self.cache = {}
        self.authors = authors
        self.words = []
        self.database()
        self.word_size = len(self.words)

    def get_random(self):
        result = []
        poets = utilities.get_poets()
        length = random.randint(1, len(poets))
        random.shuffle(poets)
        return [poet for poet in poets[:length]]
        

    def generate_markov_text(self, size=1500):
        seed = random.randint(0, self.word_size-3)
        seed_word, next_word = self.words[seed], self.words[seed+1]
        w1, w2 = seed_word, next_word
        gen_words = []

        for i in xrange(size):
            gen_words.append(w1)

            w1, w2 = w2, random.choice(self.cache[(w1, w2)])
        gen_words.append(w2)
        self.text = ' '.join(gen_words)
        return self.text

    def triples(self):
        '''
        Instead of opening text files in memory all at once, building
        a master file, splitting the text into a list of words, 
        then looping through them with a generator as class Markov does, 
        here we iterate by line and yield the appropriate tuples directly.
        '''
        if not self.authors:
            return
        else:
            result = []
            if 'Random' in self.authors:
                self.authors = self.get_random()
                print "TRUE"
            for author in self.authors:
                fname = utilities.STATIC_ROOT + '/corpus/' + author + '.txt'
                for line in open(fname):
              
                    line = formatting.split_commas(line)
                    for word in line.split():
                        word = formatting.remove_illegal_chars(word)
                        word = formatting.remove_single_letter_words(word) 
                        if word != None:
                            self.words.append(word)
                            result.insert(0, word)
                            if len(result) >= 3:
                                yield tuple(reversed(result))
                                result = result[:2]


def write(user_selection):
    is_random = False
    authors = user_selection['authors']
    if user_selection['scheme']:
        scheme = user_selection['scheme']
        length = int(user_selection[user_selection['scheme']])

    else:
        length = utilities.random_length()
        is_random = True
        
    # check if this combination of authors has been used before.
    # text = utilities.check_if_combo_exists(authors)

    # If not, create a new one.       
    # combined_text = utilities.build_mixed_corpus(authors)
    # utilities.write_combination_file(combined_text, authors)

    '''Build the markov text using one of
    the markov-generating classes.
    ''' 
    markov = MarkovGenerator(authors)
    combined_text = ''
    markov.generate_markov_text()
       
    combined_text = ''
    poem_arr = rhymer.rhyme(markov.text, length, scheme, random=is_random)

    if len(poem_arr) < 1:
        write(user_selection)
    else:
        poem = poem_arr

        '''
        save poem to the database, but also return
        the poem's id for use in url redirection
        '''
        poem_id = utilities.save_poem('^^'.join(poem))
        return dict(poem=poem, 
                    id=str(poem_id)
                )







