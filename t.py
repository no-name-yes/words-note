import sys
from PyQt6.QtWidgets import QApplication, QLineEdit, QComboBox
from PyQt6.QtCore import Qt, QTranslator, QLibraryInfo


class Translator:
    def __init__(self, app):
        self.app = app
        self.translator = QTranslator()

    def load_translations(self):
        qt_translator = QTranslator()
        if qt_translator.load(QLibraryInfo.location(QLibraryInfo.LibraryLocation.TranslationsPath),
                              'qtbase_' + self.app.locale().name(),
                              '_',
                              QLibraryInfo.location(QLibraryInfo.LibraryLocation.TranslationsPath)):
            self.app.installTranslator(qt_translator)
        if self.translator.load('translation_' + self.app.locale().name() + '.qm'):
            self.app.installTranslator(self.translator)

    def translate(self, text):
        return self.translator.translate('MainWindow', text)


class MainWindow(QLineEdit):
    def __init__(self):
        super().__init__()
        self.translator = Translator(app)
        self.translator.load_translations()
        self.combo = QComboBox(self)
        self.combo.addItems(['en', 'zh-CN', 'ja'])
        self.combo.move(10, 50)
        self.combo.currentTextChanged.connect(self.translate_text)

    def translate_text(self):
        text = self.text()
        lang = self.combo.currentText()
        self.translator.translator.load('qt_' + lang, QLibraryInfo.location(QLibraryInfo.LibraryLocation.TranslationsPath))
        self.translator.load_translations()
        self.setText(self.translator.translate(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())