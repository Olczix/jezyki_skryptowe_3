import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from py_gtk_app.change_city import ChangeCity
from utils.helpers import read_app_description
from py_gtk_app.functions import get_current_weather_text, hourly_weather_chart

  
class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title ="Prognoza pogody")
        self.set_border_width(10)
  
        # Przechowywanie układu widoku aplikacji
        self.vbox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 10)
        self.add(self.vbox)

        # Menu
        mb = Gtk.MenuBar()

        # Pierwszy przycisk menu - wysuwany
        menu1 = Gtk.Menu()
        weather = Gtk.MenuItem("Pogoda")
        weather.set_submenu(menu1)
        current_weather_menu = Gtk.MenuItem("Aktualna pogoda")
        current_weather_menu.connect("activate", self.show_current_weather)
        menu1.append(current_weather_menu)
        sep = Gtk.SeparatorMenuItem()
        menu1.append(sep)
        hourly_weather = Gtk.MenuItem("Pogoda na 24h")
        hourly_weather.connect("activate", self.show_hourly_weather)
        menu1.append(hourly_weather)

        # Drugi przycisk menu
        city = Gtk.MenuItem("Zmień nazwę miasta")
        city.connect("activate", self.show_city_input)

        # Trzeci przycisk menu
        about_app = Gtk.MenuItem("O aplikacji")
        about_app.connect("activate", self.show_author_info)

        # Dodanie przycisków do menu
        mb.append(weather)
        mb.append(city)
        mb.append(about_app)
        self.vbox.pack_start(mb, False, False, 0)

        # DOdanie wszystkich widoków aplikacji
        self.stack = Gtk.Stack()
        label = Gtk.Label(get_current_weather_text())
        label.set_justify(Gtk.Justification.LEFT)
        self.stack.add_named(label, "current_weather")
        self.stack.add_named(ChangeCity(self).grid, "change_city")
        self.stack.add_named(Gtk.Label(read_app_description()), "about_app")
  
        # Ustawienie przełączania pomiędzy widokami aplikacji
        self.stack_switcher = Gtk.StackSwitcher()
        self.stack_switcher.set_stack(self.stack)
        self.vbox.pack_start(self.stack_switcher, False, False, 0)
        self.vbox.pack_start(self.stack, True, False, 0)

    def show_current_weather(self, _):
        self.stack.get_child_by_name("current_weather").set_markup(get_current_weather_text())
        self.stack.set_visible_child(self.stack.get_child_by_name("current_weather"))

    def show_hourly_weather(self, _):
        hourly_weather_chart()

    def show_city_input(self, _):
        self.stack.get_child_by_name("current_weather").set_markup(get_current_weather_text())
        self.stack.set_visible_child(self.stack.get_child_by_name("change_city"))

    def show_author_info(self, _):
        self.stack.set_visible_child(self.stack.get_child_by_name("about_app"))


def start_app():
    win = MyWindow()
    win.connect("destroy", Gtk.main_quit)
    win.set_default_size(650, 550)
    win.show_all()
    Gtk.main()
