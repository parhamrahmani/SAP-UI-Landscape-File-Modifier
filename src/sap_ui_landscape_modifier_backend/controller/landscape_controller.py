from duplication_handler import DuplicateManager
from src.sap_ui_landscape_modifier_backend.xml_query import XMLQuery
from uuid_manager import UUIDManager
from xml_parser import XMLHandler

class LandscapeController:
    def __init__(self, source_path, destination_path):
        # Initialize XML handlers
        self.source_xml = XMLHandler(source_path)
        self.destination_xml = XMLHandler(destination_path)

        # Initialize managers
        self.source_xml_query = XMLQuery(self.source_xml.root)
        self.destination_xml_query = XMLQuery(self.destination_xml.root)
        self.uuid_manager = UUIDManager(self.destination_xml.root)
        self.duplicate_manager = DuplicateManager(self.destination_xml.root)