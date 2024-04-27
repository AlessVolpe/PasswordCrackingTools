import string
from collections import Counter


class AnalizerFunctions:
    def __init__(self):
        self.__lower = list(string.ascii_lowercase)
        self.__upper = [x.upper() for x in self.__lower]
        self.__digits = list(str(range(10)))

    # region Properties
    @property
    def __lower(self):
        return self.__lower

    @property
    def __upper(self):
        return self.__upper

    @property
    def __digits(self):
        return self.__digits

    # endregion

    def __split(self, word):
        return list(word)

    def __converter(self, password):
        split_password = self.__split(password)
        converted_splitword = []
        for i in range(0, len(password)):
            password_char = split_password[i]
            match password_char:
                case password_char if password_char in self.__lower:
                    converted_splitword.append("?l")
                case password_char if password_char in self.__upper:
                    converted_splitword.append("?u")
                case password_char if password_char in self.__digits:
                    converted_splitword.append("?d")
                case _:
                    converted_splitword.append("?s")

        return converted_splitword

    def __word_list_appender(self, wordfile):
        converted_wordlist = []
        for word in map(self.__converter, wordfile):
            converted_wordlist.append("".join(word))

        return converted_wordlist

    def top_x(self, wordlist, num):
        """
        Method that returns the x most common masks in the wordlist file
        
        Args:
            :param AnalizerFunctions self:
            :param str wordlist: /path_to/wordlist_file
            :param int num: the number of masks to show
        
        Returns:
            :ret list[tuple[Any, int]] list of the x most common masks
        """
        masterlist = self.__word_list_appender(wordlist)
        counter = Counter(masterlist)

        return counter.most_common(num)
