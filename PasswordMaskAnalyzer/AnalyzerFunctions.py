import string
from collections import Counter

class AnalizerFunctions:
    def __init__(self):     
        self._lower = list(string.ascii_lowercase)
        self._upper = [x.upper() for x in self._lower]
        self._digits = list(str(range(10)))

    #region Properties
    @property
    def lower(self):
        return self._lower
    
    @property
    def upper(self):
        return self._upper
    
    @property
    def digits(self):
        return self._digits
    #endregion
    
    def split(self, word):
        return [char for char in word]

    def converter(self, password):
        split_password = self.split(password)
        converted_splitword = []
        for i in range(0, len(password)):
            password_char = split_password[i]
            
            match password_char:
                case password_char if password_char in self.lower:
                    converted_splitword.append('?l')
                case password_char if password_char in self.upper:
                    converted_splitword.append('?u')
                case password_char if password_char in self.digits:
                    converted_splitword.append('?d')
                case _:
                    converted_splitword.append('?s')
                        
        return converted_splitword       

    def wordListAppender(self, wordfile):
        converted_wordlist = []
        for word in map(self.converter, wordfile):
            converted_wordlist.append(''.join(word))

        return converted_wordlist

    def topX(self, wordlist, num):
        masterlist = self.wordListAppender(wordlist)
        counter = Counter(masterlist)
        
        return counter.most_common(num)