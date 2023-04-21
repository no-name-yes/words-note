import sys
from PyQt6.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QMessageBox, QMainWindow)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QDateTime

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.statusBar().showMessage("Ready")

        #初始化日期
        now_detail_timedate=QDateTime.currentDateTime().toString()

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        #按钮初始化
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(100, 50)

        self.setGeometry(600, 600, 600, 300)
        self.setWindowTitle('Ttestwindows')
        self.show()

    def close(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.StandardButton.Yes |
                                     QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:

            event.accept()
        else:

            event.ignore()



def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()