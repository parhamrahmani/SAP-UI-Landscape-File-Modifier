import tkinter as tk
from tkinter import ttk
from src.sap_ui_landscape_modifier_gui.conf.guiproperties import GuiProperties as gp

class MainMenuPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configure the grid layout for MainMenuPage
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create content_frame to hold all widgets
        content_frame = tk.Frame(self)
        content_frame.grid(row=0, column=0, sticky='nsew')
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)

        # Inner frame to hold the widgets
        inner_frame = tk.Frame(content_frame)
        inner_frame.grid(row=0, column=0)
        inner_frame.grid_rowconfigure(0, weight=1)
        inner_frame.grid_columnconfigure(0, weight=1)

        # Main title
        title_label = tk.Label(
            inner_frame,
            text=gp.TITLE,
            font=gp.FONT_BOLD,
            anchor='center'
        )
        title_label.grid(row=0, column=0, pady=(20, 10), sticky='nsew')

        # Warning message
        warning_label = tk.Label(
            inner_frame,
            text="Please make sure to have a backup of your Landscape files before using the tool!",
            fg="red",
            font=gp.FONT,
            wraplength=600,
            justify="center",
            anchor='center'
        )
        warning_label.grid(row=1, column=0, pady=(0, 20), sticky='nsew')

        # Frame for buttons
        button_frame = tk.Frame(inner_frame)
        button_frame.grid(row=2, column=0, sticky='nsew')
        button_frame.grid_columnconfigure(0, weight=1)

        # List of options and their corresponding page names or commands
        options = gp.MENU_OPTIONS + [("Exit", self.exit_app)]

        # Create buttons for each option using tk.Button
        for idx, (option_text, action) in enumerate(options):
            if callable(action):
                command = action
            else:
                command = lambda page_name=action: controller.show_page(page_name)

            btn = gp.setButtonProperties(button_frame, option_text, command, gp.FONT)
            btn.grid(row=idx, column=0, pady=5, sticky='nsew')

        # Configure grid weights for buttons to expand
        for idx in range(len(options)):
            button_frame.grid_rowconfigure(idx, weight=1)
        button_frame.grid_columnconfigure(0, weight=1)

        # Adjust inner_frame to center vertically and horizontally
        inner_frame.update_idletasks()
        total_height = inner_frame.winfo_reqheight()
        total_width = inner_frame.winfo_reqwidth()
        window_height = self.controller.winfo_height()
        window_width = self.controller.winfo_width()
        if window_height == 1:
            window_height = self.controller.winfo_reqheight()
        if window_width == 1:
            window_width = self.controller.winfo_reqwidth()
        padding_y = max((window_height - total_height) // 2, 20)
        padding_x = max((window_width - total_width) // 2, 20)
        inner_frame.grid_configure(padx=padding_x, pady=padding_y)

    def exit_app(self):
        """Exit the application."""
        self.controller.quit()
