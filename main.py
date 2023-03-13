from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import time


class TranslatorWindow(QMainWindow):
    def __init__(self):
        super(TranslatorWindow,self).__init__()
        self.initUI()
        self.timer_start = 0
        self.timer_end = 0
        self.code = "Code : "
        self.translator_dict = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}


    def calculate_time(self):
        return self.timer_end - self.timer_start

    def timerStart(self):
        self.timer_start = time.perf_counter()

    def timerEnd(self):
        self.timer_end = time.perf_counter()
        time_taken = self.calculate_time()
        print(time_taken)
        self.write_code(time_taken)

    def write_code(self, time_taken):
        if time_taken <= 0.2:
            self.code = self.code + "."
        else:
            self.code = self.code + "-"
        self.print_code()

    def write_space(self):
        self.code = self.code + " "
        self.print_code()

    def write_slash(self):
        self.code += "/"
        self.print_code()

    def reset_code(self):
        self.code = "Code : "
        self.print_code()

    def print_code(self):
        self.label.setText(self.code)

    def translate_code(self, code):
        code = code.split(" ")
        translation = ""
        for char in code:
            translation += self.translator_dict[char]
        return translation



    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Translator")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Code : ")
        self.label.setFixedWidth(500)
        self.label.move(5,37)

        self.record_button = QtWidgets.QPushButton(self)
        self.record_button.setText("Record")
        self.record_button.pressed.connect(self.timerStart)
        self.record_button.released.connect(self.timerEnd)

        self.space_button = QtWidgets.QPushButton(self)
        self.space_button.setText("Space")
        self.space_button.clicked.connect(self.write_space)
        self.space_button.move(100, 0)

        self.next_word_button = QtWidgets.QPushButton(self)
        self.next_word_button.setText("Next Word")
        self.next_word_button.clicked.connect(self.write_slash)
        self.next_word_button.move(200, 0)

        self.reset_code_button = QtWidgets.QPushButton(self)
        self.reset_code_button.setText("Reset Code")
        self.reset_code_button.clicked.connect(self.reset_code)
        self.reset_code_button.move(0, 75)




def window():
    app = QApplication(sys.argv)
    translator_win = TranslatorWindow()
    translator_win.show()
    sys.exit(app.exec_())

window()
