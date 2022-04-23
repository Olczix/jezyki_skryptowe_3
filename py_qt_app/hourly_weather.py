from PyQt5.QtWidgets import QWidget
from utils.helpers import read_file
from py_qt_app.functions import get_hourly_weather_list
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MyCanvas(FigureCanvas):
    def __init__(self, parent):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        self.setParent(parent)
        self.draw_plot()
        plt.ion()

    def draw_plot(self):
        x = [obj.hour for obj in get_hourly_weather_list()[2:26]]
        y = [float(obj.temp) for obj in get_hourly_weather_list()[2:26]]
        self.ax.bar(x, y)
        for i in range(len(x)):
            plt.text(i, y[i] + 0.05, round(y[i], 1), ha='center', fontsize=7)
        self.ax.set_ylim(min(y) - 1, max(y) + 1)
        self.ax.set(xlabel="Godziny", ylabel="Temperatura [\u00b0C]")
        self.ax.set(title=f"Temperatura godzinowa dla miasta {read_file().upper()}")
        self.ax.tick_params(axis="x", rotation=50)

    def update(self):
        self.ax.cla()
        self.draw_plot()


class HourlyWeather(QWidget):
    def __init__(self):
        super().__init__()
        self.chart = MyCanvas(self)
