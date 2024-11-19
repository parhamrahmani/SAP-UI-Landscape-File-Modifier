from lxml import etree
import logging

logger = logging.getLogger(__name__)

class XMLParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tree = None
        self.root = None

        # Parse the XML file
        self.parse_xml_file()
        
    def parse_xml_file(self):
        logger.info(f"Parsing XML file: {self.file_path}")

        try:
            self.tree = etree.parse(self.file_path)
            self.root = self.tree.getroot()
            logger.info(f"Parsed XML file: {self.file_path}")
        except FileNotFoundError:
            logger.error(f"File not found: {self.file_path}")
            raise
        except etree.XMLSyntaxError as e:
            logger.error(f"Syntax error in XML file: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error while parsing XML file: {e}")
            raise

    def save_xml(self, output_path=None):
        if output_path is None:
            output_path = self.file_path

        try:
            self.tree.write(output_path, pretty_print=True, xml_declaration=True, encoding='UTF-8')
            logger.info(f"Saved XML file to: {output_path}")
        except Exception as e:
            logger.error(f"Error while saving XML file: {e}")
            raise