from PyQt5.QtWidgets import QWidget, QFormLayout, QLabel
from py_qt_app.functions import get_current_weather_obj
from utils.helpers import read_file
from PyQt5.QtCore import Qt


class CurrentWeather(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aktualna pogoda")
        self.resize(270, 110)

        self.layout = QFormLayout()
        self.layout.setFormAlignment(Qt.AlignCenter)
        self.label = QLabel()
        self.label.setText(self.get_current_weather_text())
        # self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter )
        self.layout.addRow(self.label)
        self.setLayout(self.layout)

    def refresh(self):
        self.label.setText(self.get_current_weather_text())

    @staticmethod
    def get_current_weather_text():
        weather_obj = get_current_weather_obj()
        info = f"Aktualna pogoda dla miasta {read_file().upper()}:\n\n" \
            f"Ogólne warunki: {weather_obj.main_weather} ({weather_obj.weather_description})\n\n" \
            f"Zachmurzenie wynosi {weather_obj.clouds}%\n" \
            f"Aktualna temperatura wynosi {weather_obj.temp}\u00b0C (odczuwalne {weather_obj.feels_like}\u00b0C)\n" \
            f"Wiatr osiąga prędkość {weather_obj.wind_speed}m/s ({weather_obj.wind_speed_converted}km/h)\n" \
            f"Ciśnienie jest równe {weather_obj.pressure} hPa\n" \
            f"Wilgotność powietrza wynosi {weather_obj.humidity}%\n" \
            f"\nOstatnia aktualizacja: {weather_obj.time} UTC"
        return info
