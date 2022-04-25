from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, \
    QPushButton, QLabel
from utils.helpers import write_to_file, read_file
from py_qt_app.functions import info_box


class ChangeCity(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zmiana miasta")
        self.resize(270, 110)

        self.layout = QFormLayout()
        label = QLabel("Podaj nazwę miasta, dla którego chcesz zobaczyć prognozę pogody:")
        self.layout.addRow(label)

        self.city_input = QLineEdit()
        self.layout.addRow(self.city_input)

        btn = QPushButton("Zapisz miasto")
        btn.pressed.connect(self.change_city)
        self.layout.addRow(btn)

        self.setLayout(self.layout)

    def change_city(self):
        write_to_file(self.city_input.text())
        info_box(f"Aktualne miasto to {read_file().upper()}.")
        self.city_input.clear()
