from collections import Counter
import json
from db import Document
from sqlalchemy.sql import func
import math
import string


class Count:

    def __init__(self, file_text, session):
        self.file_text = self.get_arr_of_words(file_text)
        self.session = session
        self.count_words()
        
    def count_words(self):
        common_words = Counter(self.file_text).most_common(50)
        count = sum(Counter(self.file_text).values())
        self.common_words = common_words
        self.count = count

    def get_arr_of_words(self, file_text):
        symbols = str.maketrans(dict.fromkeys(string.punctuation))
        res = file_text.translate(symbols)
        arr_of_words = res.split()
        arr_of_words_filtered = list(filter(lambda a: len(a)>=3, arr_of_words))
        print(arr_of_words_filtered)
        return arr_of_words_filtered

    def count_tf(self):
        arr_of_tf = list(map(lambda a: round(a[1]/self.count, 10), self.common_words))
        return arr_of_tf

    def count_idf(self, word):
        count_of_all_docs = self.session.query(Document).count()
        condition = [func.strpos(Document.file_text, word) > 0]
        count_of_docs_with_word = self.session.query(Document).filter(*condition).count()
        if count_of_docs_with_word == 0:
            return 0
        idf = math.log10(count_of_all_docs/count_of_docs_with_word)
        return idf

    def get_idf(self):
        arr_of_words = list(map(lambda a: a[0], self.common_words))
        arr_of_idf = list(map(self.count_idf, arr_of_words))
        return arr_of_idf

    def get_words(self):
        new_arr = list(map(lambda a: a[0], self.common_words))
        return new_arr

    def make_json(self):
        result = []
        arr_of_tf = self.count_tf()
        arr_of_idf = self.get_idf()
        for i in range(len(self.common_words)):
            arr = []
            arr.append(arr_of_tf[i])
            arr.append(arr_of_idf[i])
            result.append(arr)
        obj = dict(zip(self.get_words(), result))
        result = dict(sorted(obj.items(), key=lambda a: a[1][1], reverse=True))
        return json.dumps(result, ensure_ascii=False)








