import re

class Cipher(object):
    def __init__(self):
        self.re = re.compile("([^a-zA-Z])")

    def encode(self, phrase, shift = 1):
        shift = shift % 26
        if self.re.search(phrase) != None:
            raise Exception("Errort: not valid string")
        else:
            return "".join([( chr(ord(ch) + shift - 26) if ord(ch) + shift > ord('z') else chr(ord(ch) + shift)) for ch in list(phrase.lower())])

    def decode(self, phrase, shift=1):
        return self.encode(phrase,  -shift )


#cls = Cipher();
#shift = 1
#enc =  cls.encode("BcDeFgHiJk", shift)
#dec =  cls.decode("c")
#print("{0}-{1}".format( enc, dec))







