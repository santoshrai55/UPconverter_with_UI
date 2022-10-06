from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 300)
        self.setWindowTitle("Unicode to Preeti Converter")
        self.setContentsMargins(20, 20, 20, 20)

        input = QLineEdit()
