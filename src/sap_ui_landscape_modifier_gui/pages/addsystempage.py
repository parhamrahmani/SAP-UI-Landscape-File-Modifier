import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from src.sap_ui_landscape_modifier_gui.conf.guiproperties import GuiProperties as gp

class AddSystemPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Title
        title_label = ttk.Label(self, text="Add a System", font=gp.FONT_BOLD)
        title_label.pack(pady=20)

        # Instructions
        instruction_label = ttk.Label(
            self,
            text="Select the source and destination Landscape files to add a system.",
            wraplength=500
        )
        instruction_label.pack(pady=10)

        # Source file selection
        source_button = ttk.Button(self, text="Select Source Landscape File", command=self.select_source_file)
        source_button.pack(pady=5)

        self.source_file_label = ttk.Label(self, text="No file selected.")
        self.source_file_label.pack(pady=5)

        # Destination file selection
        dest_button = ttk.Button(self, text="Select Destination Landscape File", command=self.select_dest_file)
        dest_button.pack(pady=5)

        self.dest_file_label = ttk.Label(self, text="No file selected.")
        self.dest_file_label.pack(pady=5)

        # Proceed button
        proceed_button = ttk.Button(self, text="Add System", command=self.add_system)
        proceed_button.pack(pady=20)

        # Back button
        back_button = ttk.Button(self, text="Back to Main Menu", command=lambda: controller.show_page("MainMenuPage"))
        back_button.pack(pady=10)

        # Variables to store file paths
        self.source_file = None
        self.dest_file = None

    def select_source_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Source Landscape File",
            filetypes=[("XML Files", "*.xml")]
        )
        if file_path:
            self.source_file = file_path
            self.source_file_label.config(text=f"Selected: {file_path}")

    def select_dest_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Destination Landscape File",
            filetypes=[("XML Files", "*.xml")]
        )
        if file_path:
            self.dest_file = file_path
            self.dest_file_label.config(text=f"Selected: {file_path}")

    def add_system(self):
        if not self.source_file or not self.dest_file:
            messagebox.showwarning("Warning", "Please select both source and destination files.")
            return

        # Call the backend function to add the system
        try:
            from sap_ui_landscape_modifier_backend.controller.landscape_controller import add_system
            add_system(self.source_file, self.dest_file)
            messagebox.showinfo("Success", "System added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
