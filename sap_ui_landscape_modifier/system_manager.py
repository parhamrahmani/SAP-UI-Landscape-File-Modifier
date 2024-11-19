import logging

logger = logging.getLogger(__name__)

class SystemManager:
    def __init__(self, xml_root):
        self.root = xml_root

    def find_system(self, server_address, system_id):
        # Build XPath expression to find a system by server_address
        xpath_expr = f".//Service[@server='{server_address}']"
        services = self.root.findall(xpath_expr)

        if not services:
            return Exception(f"System with server address '{server_address}' not found.")

    