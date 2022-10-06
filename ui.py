# from curses import window
from queue import Empty
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QPlainTextEdit
from PyQt6.QtGui import QFont
import sys
from converter import converter
from data import data_set


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.resize(700, 500)
        self.setWindowTitle("Unicode to Preeti Converter")
        self.setContentsMargins(20, 20, 20, 20)
        self.setStyleSheet("background-color: #f8f8f8; border-radius:5px")
        self.text_editor()
        self.show_result()
        self.btn()
        self.show()

    def show_result(self):
        self.output = QPlainTextEdit(self)
        self.output.setStyleSheet(
            "background-color:  #fff; padding: 5px; color: #666666")
        self.output.resize(680, 200)
        self.output.setFont(QFont("Preeti", 16))
        self.output.move(10, 290)

    def text_editor(self):
        title = QLabel(self)
        title.setText("unicode to preeti")
        title.setFont(QFont("Arial", 10))
        title.setStyleSheet("color: #666666;")
        title.move(200, 28)
        title_span = QLabel(self)
        title_span.setText("Converter")
        title_span.setStyleSheet("color: #26a69a;")
        title_span.setFont(QFont("Arial", 17))
        title_span.move(300, 20)

        self.input = QPlainTextEdit(self)
        self.input.setStyleSheet(
            "background-color:  #fff; padding: 5px; color: #666666;")
        self.input.setPlaceholderText("Paste or Type Unicode Text Here")
        self.input.setFont(QFont("Kokila", 16))
        self.input.resize(680, 200)
        self.input.move(10, 50)

    def myconverter(self):
        input_text = self.input.toPlainText()
        self.result = converter(input_text, data_set)
        self.output.setPlainText(self.result)

    def btn(self):
        mybtn = QPushButton("CONVERT", self)
        mybtn.setFixedWidth(100)
        mybtn.setStyleSheet(
            "background-color:  #26a69a; padding: 5px; color: #fff;")
        mybtn.setFont(QFont("Arial", 12))
        mybtn.clicked.connect(self.myconverter)
        mybtn.move(280, 255)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
