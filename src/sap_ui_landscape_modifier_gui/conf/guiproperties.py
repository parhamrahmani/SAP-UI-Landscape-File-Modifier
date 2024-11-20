import tkinter as tk
from tkinter import ttk
from tkinter import font

class GuiProperties:
    def __init__(self):
        self.btn_font = ("Ubuntu Medium", 12)
    
    TITLE="SAP UI Landscape File Modifier"
    APP_SIZE="600x550"
    FONT=("Ubuntu Medium", 12)
    FONT_BOLD=("Ubuntu Medium", 12, "bold")
    MENU_OPTIONS = [
            ("Add a System (from a Landscape to another Landscape file)", "AddSystemPage"),
            ("Remove a System in a Landscape File", "RemoveSystemPage"),
            ("Modify a System in a Landscape File", "ModifySystemPage"),
            ("Regenerate UUIDs in a Landscape File", "RegenerateUUIDsPage"),
            ("Export Excel Reports from a Landscape File", "ExportExcelPage"),
            ("Remove Duplication from a Landscape File (Use with Caution!)", "RemoveDuplicationPage"),
            ("Consistency Check", "ConsistencyCheckPage")
        ]
    
    def setButtonProperties(frame, text, command, font):
        button = tk.Button(
            frame,
            text=text,
            command=command,
            wraplength=600,
            justify='center',
            anchor='center',
            font=font,
            padx=10,
            pady=5
            )
        return button	

