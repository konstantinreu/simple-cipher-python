import re

class Cipher(object):
    def __init__(self):
        self.re = re.compile("([^a-z])")

    def Encrypt(self, phrase, shift):
        shift = shift % 26
        if self.re.match(phrase) != None:
            raise Exception("Errort: not valid string")
        else:
            return "".join([( chr(ord(ch) + shift - 26) if ord(ch) + shift > ord('z') else chr(ord(ch) + shift)) for ch in list(phrase.lower())])

cls = Cipher();
print ( cls.Encrypt("abcdefghijklmnopqrstuvwxyz", 1) )






