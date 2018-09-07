from arabic_pronounce import phonetise
import argparse

def to_arpa(ar):
    arr = []
    for word in ar.split(' '):
      if word in [" ", ""]:
        pass
      elif word in [",", '.', '-']:
        x = word
        arr.append(x)
      else:
        x = _maybe_get_arpabet(word)
        arr.append(x)
    text = ' '.join(arr)
    print(text)
    return text

def _maybe_get_arpabet(word):
    pronunciations = phonetise(word)
    toBeReturned = '{%s}' % pronunciations[0] if len(pronunciations)==1 else '{%s}' % pronunciations[1]
    return toBeReturned
