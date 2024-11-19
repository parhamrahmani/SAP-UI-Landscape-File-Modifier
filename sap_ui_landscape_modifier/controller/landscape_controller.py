from duplication_handler import DuplicateManager
from system_manager import SystemManager
from uuid_manager import UUIDManager
from xml_parser import XMLHandler

class LandscapeController:
    def __init__(self, source_path, destination_path):
        # Initialize XML handlers
        self.source_xml = XMLHandler(source_path)
        self.destination_xml = XMLHandler(destination_path)

        # Initialize managers
        self.source_system_manager = SystemManager(self.source_xml.root)
        self.destination_system_manager = SystemManager(self.destination_xml.root)
        self.uuid_manager = UUIDManager(self.destination_xml.root)
        self.duplicate_manager = DuplicateManager(self.destination_xml.root)