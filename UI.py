import sys
import PyQt6.QtWidgets
from PyQt6.QtCore import QDate, QDateTime, QTime, Qt, QTimer, QSortFilterProxyModel
from local_data import Wordsdata
#from translate_module import Translate_class
#from Tetris import Tetris  #copy的俄罗斯方块小游戏
class MAINUI(PyQt6.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # init the homepage
        self.setGeometry(500, 300, 550, 400)
        self.setWindowTitle('homepage')

        # widget of homepage
        # init
        #button and calendar
        quitbtn = PyQt6.QtWidgets.QPushButton('Exit',self)
        quitbtn.clicked.connect(self.exitEvent) #未修改之前quitbtn.clicked.connect(PyQt6.QtWidgets.QApplication.instance().quit)
        quitbtn.resize(quitbtn.sizeHint())
        self.schedule_btn = PyQt6.QtWidgets.QPushButton('schedule', self)
        self.schedule_btn.clicked.connect(self.schedule_windows)
        self.addwordbtn = PyQt6.QtWidgets.QPushButton('addword', self)
        self.addwordbtn.clicked.connect(self.addword)

        #翻译类实例初始化
        #trans_class = Translate_class


        #俄罗斯方块小游戏暂时搁置未添加
        #self.Tetris = PyQt6.QtWidgets.QPushButton('俄罗斯方块', self)
        #self.Tetris.clicked.connect(self.startofTetris)  #启动俄罗斯方块小游戏

        #tooltips
        self.schedule_btn.setToolTip('The palce is <b>not</b> complete')
        self.addwordbtn.setToolTip('a case(need to modify)')

        #statusbar



        #line_edit
        self.searchline = PyQt6.QtWidgets.QLineEdit(self)
        self.searchline.setFrame(False)
        self.searchline.setClearButtonEnabled(True)
        self.searchline.setPlaceholderText('Search words here')
        #self.searchline.setStyle()
        #simp to add a word by other way(uncomplete)
        self.addwordbtn_simp = PyQt6.QtWidgets.QLineEdit(self)
        self.addwordbtn_simp.setPlaceholderText('add a new word')

        #completer
        file = Wordsdata()
        file.read_file_to_completer()
        self.searchcompleter = PyQt6.QtWidgets.QCompleter(file.completerwords)
        self.searchcompleter.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)#不区分大小写

        self.searchline.setCompleter(self.searchcompleter)#将self.searchcompleter设置为searchline的补全器


        #time
        self.dt = QDateTime.currentDateTime()
        self.dt_lable = PyQt6.QtWidgets.QLabel(self.dt.toString(), self)
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.updatetime)

        # beautify the UI(picture etc...)


        # layout (temp)
        uiHlayout = PyQt6.QtWidgets.QHBoxLayout()
        uiVlayout = PyQt6.QtWidgets.QVBoxLayout()
        uiHlayout.addStretch(1)
        uiHlayout.addWidget(self.schedule_btn)  #schedule按钮暂用位置
        uiHlayout.addWidget(self.addwordbtn_simp) #addwordbtn_simp添加生词暂用位置
        uiHlayout.addStretch(1)

        uiHlayout.addLayout(uiVlayout)
        uiVlayout.addWidget(self.searchline)
        uiVlayout.addStretch(1)
        uiVlayout.addWidget(quitbtn)
        uiVlayout.addWidget(self.dt_lable)


        # update the label of timelayout
        self.setLayout(uiHlayout)

        self.show()

    def updatetime(self):
        self.dt = QDateTime.currentDateTime()
        self.dt_lable.setText(self.dt.toString())

    def schedule_windows(self):
        self.schedule_w = Window_schedule()
        self.schedule_w.show()

    def exitEvent(self, event):  #退出确认事件
        reply = PyQt6.QtWidgets.QMessageBox.question(self, '跑🔨，快来多看几个单词' , 'Are you sure about that?',
        PyQt6.QtWidgets.QMessageBox.StandardButton.Yes|PyQt6.QtWidgets.QMessageBox.StandardButton.Close, PyQt6.QtWidgets.QMessageBox.StandardButton.Close)

        if reply == PyQt6.QtWidgets.QMessageBox.StandardButton.Yes:
            PyQt6.QtWidgets.QApplication.instance().quit()

    #add word dialog
    def addword(self):
        addworddialog = PyQt6.QtWidgets.QDialog(self)
        addworddialog.setWindowTitle('Add the raw word to the note')
        addworddialog.setGeometry(500,300,600,400)
        self.labletip = PyQt6.QtWidgets.QLabel('this is a test status')
        self.commit_btn = PyQt6.QtWidgets.QPushButton('commit', self)

        self.addwordlineIn_english = PyQt6.QtWidgets.QLineEdit(self)
        self.addwordlineIn_soundmark = PyQt6.QtWidgets.QLineEdit(self)
        self.addwordlineIn_japanese = PyQt6.QtWidgets.QLineEdit(self)
        self.addwordlineIn_jiaming = PyQt6.QtWidgets.QLineEdit(self)
        self.addwordlineIn_chinese = PyQt6.QtWidgets.QLineEdit(self)
        self.addwordlineIn_pingyin = PyQt6.QtWidgets.QLineEdit(self)
        self.addwordlineIn_cixing = PyQt6.QtWidgets.QLineEdit(self)
        self.addwordlineIn_english.setPlaceholderText('here to input english')
        self.addwordlineIn_soundmark.setPlaceholderText('here to input pronunciation')
        self.addwordlineIn_japanese.setPlaceholderText('here to input 日本語')
        self.addwordlineIn_jiaming.setPlaceholderText('here to input 発音')
        self.addwordlineIn_chinese.setPlaceholderText('here to input 中文')
        self.addwordlineIn_pingyin.setPlaceholderText('here to input pingyin')
        self.addwordlineIn_cixing.setPlaceholderText('here to input 词性')


        #addword_window layout
        self.addword_layout = PyQt6.QtWidgets.QVBoxLayout()
        self.addword_layout.addWidget(self.addwordlineIn_english)
        self.addword_layout.addWidget(self.addwordlineIn_soundmark)
        self.addword_layout.addWidget(self.addwordlineIn_japanese)
        self.addword_layout.addWidget(self.addwordlineIn_jiaming)
        self.addword_layout.addWidget(self.addwordlineIn_chinese)
        self.addword_layout.addWidget(self.addwordlineIn_pingyin)
        self.addword_layout.addWidget(self.addwordlineIn_cixing)
        self.addword_layout.addStretch(1)
        self.addword_Hlayout = PyQt6.QtWidgets.QHBoxLayout()
        self.addword_Hlayout.addStretch(1)
        self.addword_layout.addLayout(self.addword_Hlayout)
        self.addword_Hlayout.addStretch(1)
        self.addword_layout.addWidget(self.commit_btn)
        #self.commit_btn.clicked.connect()   #提交新的单词给本地库(还未有事件响应函数)
        addworddialog.setLayout(self.addword_layout)
        addworddialog.exec()





class Window_schedule(PyQt6.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,300,300)
        self.layout = PyQt6.QtWidgets.QHBoxLayout()
        self.schedule = PyQt6.QtWidgets.QCalendarWidget(self)
        self.layout.addWidget(self.schedule)
        self.setLayout(self.layout)



def main():
    app = PyQt6.QtWidgets.QApplication(sys.argv)
    ui = MAINUI()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
