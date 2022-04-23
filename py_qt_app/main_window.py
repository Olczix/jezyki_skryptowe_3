import sys
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, \
    QStackedLayout, QPushButton, QLabel, QWidget, QApplication
from py_qt_app.change_city import ChangeCity
from py_qt_app.hourly_weather import HourlyWeather
from py_qt_app.current_weather import CurrentWeather
from utils.helpers import read_app_description


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.setWindowTitle("Aplikacja pogodowa")
        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()
        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)

        btn = QPushButton("Aktualna pogoda")
        btn.pressed.connect(self.show_current_weather)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(CurrentWeather())

        btn = QPushButton("Pogoda na 24h")
        btn.pressed.connect(self.show_hourly_weather)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(HourlyWeather())

        btn = QPushButton("Zmień miasto")
        btn.pressed.connect(self.show_city_input)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(ChangeCity())

        btn = QPushButton("O autorze")
        btn.pressed.connect(self.show_author_info)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(QLabel(read_app_description()))

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def show_current_weather(self):
        self.stacklayout.setCurrentIndex(0)
        self.stacklayout.currentWidget().refresh()

    def show_hourly_weather(self):
        self.stacklayout.setCurrentIndex(1)
        self.stacklayout.currentWidget().chart.update()

    def show_city_input(self):
        self.stacklayout.setCurrentIndex(2)
        self.stacklayout.currentWidget().show()

    def show_author_info(self):
        self.stacklayout.setCurrentIndex(3)


def start_app():
    app = QApplication(sys.argv)
    app.setApplicationName('Prognoza pogody')

    main = MyWindow()
    main.resize(650, 550)
    main.show()

    sys.exit(app.exec_())
