from collections import Counter

class File:
    
    def __init__(self, file, data=None):
        self.file = file
        self.data = data
        
    def get_text(self):
        reader = open(self.file, 'r', errors='ignore', encoding='utf-8')
        self.data = reader.read()
        return self.data


class Count:
    
    def __init__(self, file):
        self.file = File(file)
        self.count_words()
        
    def count_words(self):
        data = self.file.get_text().split()
        common_words = Counter(data).most_common(50)
        count = sum(Counter(data).values())
        self.common_words = common_words
        self.count = count

    def count_tf(self):
        arr = []
        for i in self.common_words:
            arr.append(round(i[1]/self.count, 10))
        return arr


class Search:
    def __init__(self):
        self.counter = Counter()


c = Count('req.txt')
common = c.common_words
# for i in common:
print(c.count_tf())
