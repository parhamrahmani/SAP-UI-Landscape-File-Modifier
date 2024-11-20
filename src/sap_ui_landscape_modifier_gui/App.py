import tkinter as tk
from src.sap_ui_landscape_modifier_gui.pages.mainmenupage import MainMenuPage
from src.sap_ui_landscape_modifier_gui.conf.guiproperties import GuiProperties as gp

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(gp.TITLE)
        self.geometry(gp.APP_SIZE)
        self.resizable(False, False)
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.frames = {}
        self.show_page("MainMenuPage")


    def show_page(self, page_name):
        """ Show a page by name"""
        if page_name not in self.frames:
            # Import the page class dynamically using the full module path
            module_name = f"src.sap_ui_landscape_modifier_gui.pages.{page_name.lower()}"
            module = __import__(module_name, fromlist=[page_name])
            page_class = getattr(module, page_name)
            page = page_class(parent=self.container, controller=self)
            self.frames[page_name] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.frames[page_name].tkraise()
