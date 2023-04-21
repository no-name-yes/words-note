import sys
import PyQt6.QtWidgets
from PyQt6.QtCore import QDate, QDateTime, QTime, Qt, QTimer, QSortFilterProxyModel
from local_data import Wordsdata

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
        #button and calender
        quitbtn = PyQt6.QtWidgets.QPushButton('Exit',self)
        quitbtn.clicked.connect(PyQt6.QtWidgets.QApplication.instance().quit)
        quitbtn.resize(quitbtn.sizeHint())
        self.schedule_btn = PyQt6.QtWidgets.QPushButton('schedule', self)
        self.schedule_btn.clicked.connect(self.schedule_windows)

        #line_edit
        self.searchline = PyQt6.QtWidgets.QLineEdit(self)
        self.searchline.setFrame(False)
        self.searchline.setClearButtonEnabled(True)
        self.searchline.setPlaceholderText('Search words here')
        #self.searchline.setStyle()

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


        # layout (temp)
        uiHlayout = PyQt6.QtWidgets.QHBoxLayout()
        uiVlayout = PyQt6.QtWidgets.QVBoxLayout()
        uiHlayout.addStretch(1)
        uiHlayout.addWidget(self.schedule_btn)  #schedule按钮暂用位置
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
