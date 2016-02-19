import re
import urllib2
import json

from random import shuffle

import formatting


def API_call(word):
    prefix = "https://api.datamuse.com/words?rel_rhy="
    response = urllib2.urlopen(prefix + word)
    return json.loads(response.read())

'''
Get all words that rhyme with
the last word in each line and
save them to prevent unnecessary
API calls. Returns an array of arrays
of all lines with their rhymes.
'''
def get_lines_arrs(lines):
    return [[break_long_sents(line, 3), API_call(line.split(' ')[-1])] for line in lines]


'''
return nested list of [line, [rhyme,],]
filtering out the 'word' value from each
rhyme dictionary.
'''
def filter_rhyme_arrs(lines_arrs):
    result = []
    for line, rhymes in lines_arrs:
        rhymes_words = []
        for rhyme_obj in rhymes:
            word = rhyme_obj['word']
            rhymes_words.append(rhyme_obj['word'])
        result.append([line, rhymes_words])
    return result
    
'''
Returns the last word and a string
containing the last two words from
each poetic line.
'''    
def get_rhyme_words(line):
    split = line.split(' ')
    return split[-1], ' '.join([split[-2], split[-1]])


'''
Break up sentences that run too long.
Usually, these will be sentences with 
many commas, as lines will have been
split on most other puntuation marks
by this point.
'''
def break_long_sents(line, allotted_commas):
    if ',' in line and len(line.split(', ')) > allotted_commas:
        split = line.split(', ')
        return ', '.join(split[:allotted_commas])
    else:
        return line
 
'''
Loop through array of [line, [rhyme,]],
and return an array of lines that rhyme with 
each other in AABB fashion.
'''
def match_rhyming_lines(arrs):
    rhyming_lines = []
    for i in range(len(arrs)-1):
        if len(arrs[i][0].split(' ')) < 2:
            pass
        else:
            first_line = arrs[i][0]
            first_last, first_last_two = get_rhyme_words(first_line)
            for j in range(len(arrs)-2):
                second_line = arrs[j][0]
                second_rhymes = arrs[j][1]
                if (first_last in second_rhymes or first_last_two in second_rhymes) and (first_line not in rhyming_lines and second_line not in rhyming_lines):
                    print first_last, first_last_two
                    print "word: " + second_line
                    rhyming_lines.append(first_line)
                    rhyming_lines.append(second_line)
                    break
    return rhyming_lines
            
'''
The rhyming array is already formatted
for AABB scheme, so we only need to worry
about the ABAB scheme here.
'''
def format_scheme(rhyming_arr, scheme):
    if scheme == 'ABAB':
        result = []
        for index in range(len(rhyming_arr)):
            if index % 3 == 0:
                result.append(rhyming_arr[index])
            result.append(rhyming_arr[index])
        return result
    else:
        return rhyming_arr

def apply_length(lines, length):
    return lines[:length]

def capitalize(lines):
    result = []
    for line in lines:
        result.append(line.strip().capitalize())
    return result

def random_lines(lines_arrs, length):
    result = []
    indexes = [i for i in range(len(lines_arrs))]
    shuffle(indexes)
    for i in indexes[:length]:
        result.append(lines_arrs[i][0])
    return result
    
           
def rhyme(text, length, scheme, random=False):
    split_text = re.split(r'[;.?!]+', text)
    lines_arrs = get_lines_arrs(split_text)
    filtered_lines_arrs = filter_rhyme_arrs(lines_arrs)  
    if random:
        print "RANDOM"
        rhymed_schemed = random_lines(filtered_lines_arrs, length)
    else:
        rhymed = match_rhyming_lines(filtered_lines_arrs)
        rhymed_schemed = format_scheme(rhymed, scheme)
    starts_with_letter = formatting.begin_with_letter(rhymed_schemed)
    final = capitalize(apply_length(starts_with_letter, length))

    
    return final
    

                
                
            

       
        
            
    
    