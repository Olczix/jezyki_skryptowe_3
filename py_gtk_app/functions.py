from utils.helpers import read_file
import matplotlib
matplotlib.use('GTK3Agg')
import matplotlib.pyplot as plt
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from py_qt_app.functions import get_hourly_weather_list
from api.weather import get_weather_by_city_name, get_hourly_weather_by_city_name
from utils.weather_object import WeatherObject


def get_current_weather_obj():
    city = read_file()
    if city != "":
        weather = get_weather_by_city_name(city)
        return WeatherObject(weather["current"])
    else:
        error_dialog("Brak zdefiniowanego miasta.\nMusisz je wybrać, aby korzystać z prognozy pogody.")

def get_hourly_weather_list():
    city = read_file()
    if city != "":
        weather = get_hourly_weather_by_city_name(city)
        weather_hourly_list = weather["hourly"]
        weather_list = []
        for weather_hourly in weather_hourly_list:
            weather_list.append(WeatherObject(weather_hourly))
        return weather_list
    else:
        error_dialog("Brak zdefiniowanego miasta.\nMusisz je wybrać, aby korzystać z prognozy pogody.")

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

def hourly_weather_chart():
    fig, ax = plt.subplots()
    x = [obj.hour for obj in get_hourly_weather_list()[2:26]]
    y = [float(obj.temp) for obj in get_hourly_weather_list()[2:26]]
    ax.bar(x, y)
    for i in range(len(x)):
        plt.text(i, y[i] + 0.05, round(y[i], 1), ha='center', fontsize=6)
    ax.set_ylim(min(y) - 1, max(y) + 1)
    ax.set(xlabel="Godziny", ylabel="Temperatura [\u00b0C]")
    ax.set(title=f"Temperatura godzinowa dla miasta {read_file().upper()}")
    ax.tick_params(axis="x", rotation=50)
    fig.show()

def info_dialog(self, message):
    dialog = Gtk.MessageDialog(
        transient_for=self, flags=0,
        message_type=Gtk.MessageType.INFO,
        buttons=Gtk.ButtonsType.OK,
        text="INFO",
    )
    dialog.format_secondary_text(message)
    dialog.run()
    dialog.destroy()

def error_dialog(self, message):
    dialog = Gtk.MessageDialog(
        transient_for=self, flags=0,
        message_type=Gtk.MessageType.ERROR,
        buttons=Gtk.ButtonsType.CANCEL,
        text="ERROR",
    )
    dialog.format_secondary_text(message)
    dialog.run()
    dialog.destroy()