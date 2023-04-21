import json
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtCore import Qt
"""
defaultdataform = {
    "english": "test",
    "soundmark": "test",
    "japanese": "test",
    "jiaming": "test",
    "chinese": "test",
    "pingyin": "test",
    "cixing": "test",
}

defaultdataform2 = {
    "english": "test2",
    "soundmark": "test2",
    "japanese": "test2",
    "jiaming": "test2",
    "chinese": "test2",
    "pingyin": "test2",
    "cixing": "test2",
}

datalist = [defaultdataform,defaultdataform2]

with open("Words_data", "w") as f:
    json.dump(datalist, f)
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



#    def write_file_to
