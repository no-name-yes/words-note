from PyQt6 import QtWidgets
import requests
import openai

class Translate_class:
    def __init__(self):
        #对控件初始化
        self.translateline = QtWidgets.QLineEdit()
        self.translatelable = QtWidgets.QLabel()
        self.translatelable.setText('result')
        #self.apiselect = QtWidgets.     #选择翻译源

        self.translateline.textChanged.connect(self.translate_evet) #每当文本改变时进行翻译

#考虑使用多种api来实现翻译功能(暂时想到google api和chatgpt来实现对翻译的对接)

    #以chatgpt作为源翻译
    def translate_evet(self, text):
        #openai.api_key =
        response = openai.Completion.create(
            engine = "text-davinci-002",
            prompt=f"翻译单词{text} 以(英文:)(英文读音:)(日文:)(日文读音:)(中文:)(拼音:)(词性:)的格式回复",
            temperature=0.5,
            max_tokens=0,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        translation_result = response.choices[0].text.strip()
        self.translatelable.setText(f'{translation_result}')#将翻译结果显示到标签中的文本显示


        #可以考虑多个label控件显示更多信息

