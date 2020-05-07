"""
This file was created for fun
Author:
    v-daeder - Dana Eder
Date:
    7/5/2020
Purpose:
    Anagram
"""
from collections import defaultdict

class Anagram:
    def __init__(self):
        pass

    def get_anagrams(self,source):
        d = defaultdict(list)
        for word in source:
            key = "".join(sorted(word))
            d[key].append((word,source.index(word)))
        return d

    def find_anagrams(self,word_source):
        d = self.get_anagrams(word_source)
        new_list=[]
        for key, anagrams in d.items():
            if len(anagrams) > 1:
                for val in anagrams:
                    new_list.insert(val[1],val[0])
        return new_list


if __name__ == '__main__':
    list_to_str = ["pool", "loco", "cool", "stain", "satin", "pretty", "nice", "loop"]
    ang=Anagram()
    print(ang.find_anagrams(list_to_str))

