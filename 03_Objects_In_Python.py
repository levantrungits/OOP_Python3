import math
from notebook import Note, Notebook

"""
    Python 3 Object-oriented Programming - Second Edition.pdf
=========================Current Page 36=====================================
"""


if __name__ == '__main__':
    n = Notebook()
    n.new_note('hello world')
    n.new_note('hello again')
    print(n.notes[0].id)