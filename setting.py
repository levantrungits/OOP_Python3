import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

DATA_TRAIN_PATH = os.path.join(DIR_PATH, '/TrungLv/Python3/OOP_Python3')
DATA_TEST_PATH = os.path.join(DIR_PATH, '/TrungLv/Python3/OOP_Python3')

DATA_TRAIN_JSON = os.path.join(DIR_PATH, '/TrungLv/Python3/OOP_Python3/data_train.json')
DATA_TEST_JSON = os.path.join(DIR_PATH, '/TrungLv/Python3/OOP_Python3/data_test.json')
STOP_WORDS = os.path.join(DIR_PATH, '/TrungLv/Python3/OOP_Python3/stopwords-nlp-vi.txt')

SPECIAL_CHARACTER = '0123456789%@$.,=+-!;/()*"&^:#|\n\t\''
DICTIONARY_PATH = '/TrungLv/Python3/OOP_Python3/dictionary.txt'