import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from utils.helpers import write_to_file, read_file
from py_gtk_app.functions import info_dialog, error_dialog
from api.geo import get_city_geo_location


class ChangeCity(Gtk.Widget):
    def __init__(self, parent_window):
        super().__init__()
        self.grid = Gtk.Grid()
        self.parent = parent_window

        self.label = Gtk.Label()
        self.label.set_markup("<big>Podaj nazwę miasta, dla którego chcesz zobaczyć prognozę pogody:</big>")
        self.grid.attach(self.label, 0, 0, 3, 1)

        self.city_input = Gtk.Entry()
        self.grid.attach(self.city_input, 0, 1, 1, 1)

        self.btn = Gtk.Button(label="Zapisz miasto")
        self.btn.connect("clicked", self.change_city)
        self.grid.attach(self.btn, 0, 2, 1, 1)
    
    def change_city(self, _):
        try:
            r = get_city_geo_location(self.city_input.get_text())
            write_to_file(self.city_input.get_text())
            info_dialog(self.parent, f"Aktualne miasto to {read_file().upper()}.")
            self.city_input.set_text('')
        except IndexError:
            error_dialog(self.parent, "Podane miasto nie jest poprawne.\nNowe miasto nie zostało zapisane do pliku.")
            self.city_input.set_text('')
