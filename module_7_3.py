class WordsFinder:
    def __init__(self, *file_names):
                                      #Объект этого класса должен принимать при создании
        self.file_names = file_names   # неограниченного количество названий файлов и
                                      # записывать их в атрибут file_names в виде списка или кортежа

    def get_all_words(self): # подготовит.метод
        all_words = {} #создать пустой словарь
        words = ""
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names: #перебрать названия файлов
            with open(file_name, 'r', encoding='utf-8') as file: # и открывать каждый из них используя with
                for line in file:
                    for punkt in punctuation:
                        line = line.replace(punkt, " ")
                    words += " " + line
                words = words.split()
                all_words[file_name] = words
        return all_words

    def find (self, word):
        result = {}
        for name, words in self.get_all_words().items():
            index = 1
            for w in words:
                if w.lower() == word.lower():
                    result[name] = index
                    break
                index +=1
        return result

    def count(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            index = 0
            for w in words:
                if w.lower() == word.lower():
                    index +=1
            result[name] = index
        return result


finder2 = WordsFinder('test_file_7_3.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего









