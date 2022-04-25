import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("Window")
        self.set_size_request(300, 300)
        self.connect("destroy", Gtk.main_quit)

        grid = Gtk.Grid()
        self.add(grid)

        menu = Gtk.Menu()
        menuitem = Gtk.MenuItem("Test1")
        menu.append(menuitem)
        menuitem.show()
        menuitem = Gtk.MenuItem("Test2")
        menuitem.show()
        menu.append(menuitem)        

        button = Gtk.Button("Test Popup")
        grid.add(button)

        button.connect_object('button-press-event', self.on_pop_menu, menu)

    def on_pop_menu(self, widget, event):
        widget.popup(None, None, None, None, event.button, event.time)

window = Window()
window.show_all()
Gtk.main()