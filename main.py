import sys
import random

from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel
from PyQt6.QtCore import pyqtSlot, Qt, QTimer


class HoverButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.defaultText = text
        self.hoverText = "Пришел"
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def enterEvent(self, event):
        super().enterEvent(event)
        self.setText(self.hoverText)

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.setText(self.defaultText)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.changeBackgroundColor)
        self.originalStyleSheet = self.styleSheet()

    def initUI(self):
        self.variableInput = QLineEdit(self)
        self.variableInput.setPlaceholderText("Введите значение x")
        self.variableInput.setValidator(QDoubleValidator())

        self.calculateButton = QPushButton('Посчитать', self)
        self.calculateButton.clicked.connect(self.calculateEquation)

        self.resultLabel = QLabel('Результат будет здесь', self)

        self.button1 = HoverButton("Ушел", self)
        self.button2 = HoverButton("Ушел", self)

        layout = QVBoxLayout(self)
        layout.addWidget(self.variableInput)
        layout.addWidget(self.calculateButton)
        layout.addWidget(self.resultLabel)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        self.setLayout(layout)
        self.setWindowTitle('Приложение на PyQt6')
        self.setGeometry(300, 300, 400, 300)

    @pyqtSlot()
    def calculateEquation(self):
        try:
            x = float(self.variableInput.text().replace(',', '.'))
            result = x ** 2 - 3 + x
            self.resultLabel.setText(f'Результат: {result}')
        except Exception as e:
            self.resultLabel.setText(f'Ошибка: {e}')

    def enterEvent(self, event):
        self.timer.start(500)

    def leaveEvent(self, event):
        self.timer.stop()
        self.setStyleSheet(self.originalStyleSheet)

    def changeBackgroundColor(self):
        color = random.choice(["#FF5733", "#33FF57", "#3357FF", "#FF33FF", "#FFFF33", "#33FFFF"])
        self.setStyleSheet(f"background-color: {color};")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
