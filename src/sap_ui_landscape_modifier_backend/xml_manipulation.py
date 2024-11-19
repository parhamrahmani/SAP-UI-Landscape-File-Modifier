
class XMLManipulation:
    def __init__(self, xml_file):

        self.xml_file = xml_file
        self.tree = None
        self.root = None

        # Parse the XML file
        self.parse_xml_file()