import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Мое приложение")
        self.setGeometry(400, 400, 280, 0)


        button = QPushButton("Нажми на меня!")
        button.setCheckable(True)
        button.clicked.connect(self.button_was_clicked)
        button.setStyleSheet("background-color: #42aaff")

        self.setMenuWidget(button)

    def button_was_clicked(self):
        print("Hello Python!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()