import json
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtCore import Qt
"""
defaultdataform = {
    "english": "test",
    "soundmark": "/tɛst/",
    "japanese": "テスト",
    "jiaming": "テスト (念作 tesuto)",
    "chinese": "测试",
    "pingyin": "cè shì",
    "cixing": "名词",
}

defaultdataform2 = {
    "english": "case",
    "soundmark": "/keɪs/",
    "japanese": "ケース",
    "jiaming": "ケース (念作 ke-su)",
    "chinese": "案例",
    "pingyin": "àn lì",
    "cixing": "名词",
}

datalist = [defaultdataform,defaultdataform2]

with open("Words_data", "w") as f:
    json.dump(datalist, f)                      #将测试数据写入实验
    """
class Wordsdata():
    def __init__(self):
        self.completerwords = []
    def read_file_to_completer(self):
        with open('Words_data', 'r', encoding='utf-8') as f:
            words = json.load(f)
            self.mode = QStandardItemModel()
        for word in words:
            self.completerwords.append(word['english'])
            self.completerwords.append(word['japanese'])
            self.completerwords.append(word['chinese'])

    def commit(self, target):
        with open("Words_data",'w',encoding='utf-8') as f:
            json.dump(target, f)


    """def write_test(self):
        with open('Words_data', 'w', encoding='utf-8') as f:
            words = json.dump(f) """



#    def write_file_to
