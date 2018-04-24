# The functions here assume input as a list of tokens (ie tokenized sentences),
# where each token was information about whether it is a word or a number.
# The text is assumed to be either japanese of English (target application is
# Japanese text which may contain English or Romanji).
#
# The token type may be (1) Hiragana   //  native Japanese words
#                       (2) Katakana   //  foreign words 
#                       (3) Kanji
#                       (4) Romaji     //  Hepburn romanization
#                       (5) English
#
#
# Dependencies: pip3 install six semidbm pykakasi



import pykakasi as pkk
import japanese_numbers as jnums
from jphones import num2kana


class Phonetizer:
    def __init__(self):
        kakasi = pkk.kakasi()
        kakasi.setMode("H","a")         # Hiragana to ascii
        kakasi.setMode("K","a")         # Katakana to ascii
        kakasi.setMode("J","a")         # Japanese to ascii
        kakasi.setMode("r","Hepburn")   # use Hepburn Roman table
        self.numConverter = num2kana.Converter()
        self.wordConverter = kakasi.getConverter()
        self.phonemes=''
        self.token=''
        self.type=''
        
    def convert_token(self, token):
        self.type=token['type']
        self.token=token['token']
        
        if token['type'] == 'word':
            self.phonemes = self.wordConverter.do(self.token)
            
        elif token['type'] == 'number':
            if ',' in self.token:
                self.token = self.token.replace(",", "")
            kana=self.numConverter.conv(jnums.to_arabic(token['token'])[0])
            self.phonemes = self.wordConverter.do(kana)


    def get_phonemes(self, token):
        self.convert_token(token)
        if self.phonemes == "NUM-TOO-LARGE":
            newToken = {'phonemes' : [self.phonemes], 'token': self.token, 'type': self.type}
        else:
            newToken = {'phonemes' : list(self.phonemes), 'token': self.token, 'type': self.type}
                    
        return newToken




def demo():

    tokens= [{'type':'word', 'token': u'日本'},
             {'type':'word', 'token': u'すごい'},
             {'type':'word', 'token': u'食べる'},
             {'type':'word', 'token': u'パソコン'},
             {'type':'word', 'token': u'Sony'},
             {'type':'number', 'token': u'32802'},
             {'type':'number', 'token': u'3,209'},
             {'type':'number', 'token': u'一〇〇'},
             {'type':'number', 'token': u'四百六十九'}] 
    
    
    
    for token in tokens:
        j2p = Phonetizer()
        phonemes = j2p.get_phonemes(token)
        print(phonemes)


if __name__ == '__main__':
    demo()
    
