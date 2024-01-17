
from textblob import Word
import re

def check_word_spelling(word):
    word = Word(word)
    result = word.spellcheck()

    if word == result[0][0]:
        return (f'Spelling of "{word}" is correct!')
    else:
        return (f'Correct spelling of "{word}":"{result[0][0]}" (with {result[0][1]} confidence).')

def check_sentence_spelling(sentence):
    words = sentence.split()
    words = [word.lower() for word in words]
    words = [re.sub(r'[^A-Za-z0-9]+', '', word) for word in words]
    
    results=[]
    for word in words:
        results.append(check_word_spelling(word))
    
    return   '\n'.join(results)  


#if __name__ == '__main__':
#    check_sentence_spelling(input(" "))