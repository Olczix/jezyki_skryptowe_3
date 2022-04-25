import sys
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, \
    QStackedLayout, QLabel, QWidget, QApplication, QMenuBar, QAction
from py_qt_app.change_city import ChangeCity
from py_qt_app.hourly_weather import HourlyWeather
from py_qt_app.current_weather import CurrentWeather
from utils.helpers import read_app_description


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.setWindowTitle("Prognoza pogody")
        pagelayout = QVBoxLayout()
        self.stacklayout = QStackedLayout()

        # Deklaracja menu
        menu_bar = QMenuBar()
        pagelayout.addWidget(menu_bar)
        
        # Pierwszy przycisk menu - wysuwany
        weather = menu_bar.addMenu("Pogoda")
        action_current_weather = QAction("Aktualna pogoda", self)
        weather.addAction(action_current_weather)
        action_current_weather.triggered.connect(self.show_current_weather)
        action_hourly_weather = QAction("Pogoda na 24h", self)
        weather.addAction(action_hourly_weather)
        action_hourly_weather.triggered.connect(self.show_hourly_weather)

        # Drugi przycisk menu
        action_change_city = QAction("Zmień nazwę miasta", self)
        menu_bar.addAction(action_change_city)
        action_change_city.triggered.connect(self.show_city_input)

        # Trzeci przycisk menu
        action_about_app = QAction("O aplikacji", self)
        menu_bar.addAction(action_about_app)
        action_about_app.triggered.connect(self.show_author_info)

        # Dodanie wszystkich widoków do layout'u
        pagelayout.addLayout(self.stacklayout)
        self.stacklayout.addWidget(CurrentWeather())
        self.stacklayout.addWidget(HourlyWeather())
        self.stacklayout.addWidget(ChangeCity())
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
