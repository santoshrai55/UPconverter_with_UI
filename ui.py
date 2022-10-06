# from curses import window
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.resize(600, 300)
        self.setWindowTitle("Unicode to Preeti Converter")
        self.setContentsMargins(20, 20, 20, 20)
        self.text_editor()
        self.btn()
        self.show()

    def text_editor(self):
        input = QLineEdit(self)
        input.move(50, 50)

    def btn(self):
        mybtn = QPushButton("Convert", self)
        mybtn.move(280, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
