'''
Sometimes, words show up with commas with no
following space like,this. Add space if there
is none.
'''
def split_commas(line):
    by_commas = line.split(',')
    return ', '.join(by_commas)

def remove_illegal_chars(word, illegals='{}[]_()/\\*$@#'):
    return word.translate(None, illegals)

'''
Ensure that the line begins with a
letter instead of punctuation, numbers, etc.
'''
def begin_with_letter(line_arr):
    result = []
    for string in line_arr:
        for i in range(len(string)):
            if string[i].isalpha():
                result.append(string[i:])
                break
    return result
            
        
'''
This is necessary because the form data
will always return the default value
of the length dropdown, even if it
hasn't been selected.
'''
def remove_duplicate_length(choices):
    scheme = choices['scheme']
    if scheme == 'AABB':
        del choices['ABAB']
    else:
        del choices['AABB']

# Filter out meaningless single-letter words.
def remove_single_letter_words(word):  
    word = word.strip() 
    if len(word) > 1 or word == 'I':
        return word
    else:
        return None
