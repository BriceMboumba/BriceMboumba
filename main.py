import numpy as np
from collections import defaultdict


def WordCount(txt):
  cpt=defaultdict(int)
  for word in txt.split():
    cpt[word]+=1
  return cpt


def map(k,v):
    intermediate=[]
    for word in v.split():
        intermediate.append((word, 1))
    return intermediate


def reduce(k, v):
    res = 0
    for count in v:
        res = res + count
    return (k, res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test = "la terre est ronde, le ciel est bleu, "
    WordCount(test)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
