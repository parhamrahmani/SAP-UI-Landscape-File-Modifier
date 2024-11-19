import uuid
import logging

logger = logging.getLogger(__name__)

class UUIDManager:
    def __init__(self, xml_root):
        self.root = xml_root

    def regenerate_uuids(self):
        elements_with_uuid = self.root.xpath('.//*[@uuid]')
        for element in elements_with_uuid:
            new_uuid = str(uuid.uuid4())
            element.set('uuid', new_uuid)
        logger.info("Regenerated UUIDs for all elements.")
