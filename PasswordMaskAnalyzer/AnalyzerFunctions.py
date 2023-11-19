import string
from collections import Counter
lower = list(string.ascii_lowercase)
upper = [x.upper() for x in lower]
digits = list(str(range(10)))

# print(str(lower) + '\n' + str(upper) + '\n' + str(digits))

def split(word):
    return [char for char in word]

def converter(password):
    split_password = split(password)
    converted_splitword = []
    for i in range(0, len(password)):
        password_char = split_password[i]
        match password_char:
            case password_char if password_char in lower:
                converted_splitword.append('?l')
            case password_char if password_char in upper:
                converted_splitword.append('?u')
            case password_char if password_char in digits:
                converted_splitword.append('?d')
            case _:
                converted_splitword.append('?s')
                    
    return converted_splitword       

def wordListAppender(wordfile):
    converted_wordlist = []
    for word in map(converter, wordfile):
        converted_wordlist.append(''.join(word))
        
    return converted_wordlist

def topX(wordlist, num):
    masterlist = wordListAppender(wordlist)
    counter = Counter(masterlist)
    return counter.most_common(num)