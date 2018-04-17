`jphones` : A Japanese Phonetizer
==============================


`jphones` accepts as input tokens of Japanese (words or numbers), and returns an approximate phonetic transcription.

The tokens can be Kanji, Harigana, Katakana, or Romaji. English words will be returned as is.

Example usage:

```
import jphones as j2p

token = {'token': 'すごい', 'type': 'word'}

phonetizer = j2p.Phonetizer()
phonemes = j2p.get_phonemes(token)

print(phonemes)
# {'phonemes': ['s', 'u', 'g', 'o', 'i'], 'token': 'すごい', 'type': 'word'}
```



Getting Started
------------------------------------


`jphones` is built upon the following Python dependencies:

- `pykakasi`
- `japanese_numbers`
- `Convert-Numbers-to-Japanese`


The `Convert-Numbers-to-Japanese` script has been significantly changed, and comes included in this repo, renamed as `num2kana.py`. No need to install anything for it.


The `japanese_numbers` module has been modified to work with `jphones` and Python3, and you should install them from my forked versions as such:

```
$ pip3 install git+https://github.com/JRMeyer/japanese-numbers-python.git
```

You can install `pykakasi` and its dependencies as such:

```
$ pip3 install six semidbm
$ pip3 install pykakasi
```





Expected Input
------------------------------------

The main `j2p.Phonetizer.get_phonemes()` function expects tokens as Python dicts. Each dict should have two entries:

- 'token': 'unicode-char-string'
- 'type': 'word' or 'number'


Returned Output
------------------------------------

The function `j2p.Phonetizer.get_phonemes()` returns the original dictionary for the token, with an extra entry for phonemes:

- 'phonemes': ['p','h','o','n','e','m','e','s']
- 'token': 'unicode-char-string'
- 'type': 'word' or 'number'



Phoneme Set
------------------------------------

The phoneme set is very naive, but for ASR it should suffice. The phonemes are a one-to-one correlate of the [Romaji Hepburn set](https://en.wikipedia.org/wiki/Hepburn_romanization).



Big Numbers
------------------------------------

Currently `jphones` can only handle numbers up to 9999. Anything larger will be returned with the phoneme-string 'NUM-TOO-LARGE'.


Licencing
------------------------------------
Of the three dependencies, only `Convert-Numbers-to-Japanese` doesn't have an MIT License. This script has no explicit license.