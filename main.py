import logging

# Configure logging at the application level
# Create a custom logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create handlers
c_handler = logging.StreamHandler()  # Console handler
f_handler = logging.FileHandler('app.log')  # File handler

# Create formatters and add them to the handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

# Import your modules after configuring logging
from src.sap_ui_landscape_modifier_backend.xml_parser import XMLParser
from src.sap_ui_landscape_modifier_gui.App import App

def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()
