import logging

class XMLQuery:

    def __init__(self, xml_root):
        self.root = xml_root
        self.logger = logging.getLogger(__name__)

    def find_system(self, server_address, system_id):
        """
        Finds a Service element based on server_address and system_id, and includes any dependencies.

        :param server_address: The server address to search for.
        :param system_id: (Optional) The system ID to search for.
        :return: A dictionary containing the found Service element and its dependencies.
        :raises Exception: If the service is not found or if there are inconsistencies.
        """

        self.logger.info(f"Finding system with server address '{server_address}' and system ID '{system_id}'")

        # Build XPath expression to find a system by server_address
        xpath_expr = f".//Service[@server='{server_address}']"
        services = self.root.findall(xpath_expr)

        if not services:
            raise Exception(f"System with server address '{server_address}' not found.")

        # Filter services by system ID
        matching_services = []
        for service in services:
            service_system_id = service.get('systemid')
            if system_id is None or service_system_id == system_id:
                matching_services.append(service)
            elif service_system_id is None:
                self.logger.warning(
                    f"Service with server address '{server_address}' doesn't have a designated system ID."
                )
                matching_services.append(service)
            else:
                self.logger.warning(
                    f"Service with server address '{server_address}' doesn't have matching system ID."
                )
                continue

        if not matching_services:
            # Services found with the server address, but system IDs differ
            found_system_ids = [service.get('systemid') for service in services]
            raise Exception(
                f"Service with server address '{server_address}' found, but system ID differs.\n"
                f"Found system IDs: {found_system_ids}"
            )

        if len(matching_services) > 1:
            self.logger.warning(
                f"Multiple services found with server '{server_address}' "
                f"and system ID '{system_id}'. Returning the first match."
            )

        found_service = matching_services[0]
        self.logger.info(f"Found service: {found_service.attrib}")

        # Check for dependencies
        dependencies = {}

        # Check for Router dependency
        router_id = found_service.get('routerid')
        if router_id:
            router = self.find_router_by_id(router_id)
            if router is not None:
                dependencies['router'] = router
            else:
                self.logger.warning(f"Router with ID '{router_id}' not found.")

        # Check for Message Server dependency
        message_server_id = found_service.get('message_server_id')
        if message_server_id:
            message_server = self.find_message_server(message_server_id)
            if message_server is not None:
                dependencies['message_server'] = message_server
            else:
                self.logger.warning(f"Message server with ID '{message_server_id}' not found.")

        return {'service': found_service, 'dependencies': dependencies}

    def find_router_by_id(self, router_id):
        """
        Finds a Router element based on router_id.

        :param router_id: The router ID to search for.
        :return: The found Router element or None.
        """
        self.logger.info(f"Finding router with ID '{router_id}'")

        routers_element = self.root.find('Routers')
        if routers_element is not None:
            for router in routers_element.findall('Router'):
                if router.get('uuid') == router_id:
                    self.logger.info(f"Found router: {router.attrib}")
                    return router
        self.logger.warning(f"Router with ID '{router_id}' not found.")
        return None

    def find_router_by_description(self, router_description):
        """
        Finds a Router element based on router_description.

        :param router_description: The router description to search for.
        :return: The found Router element or None.
        """
        self.logger.info(f"Finding router with description '{router_description}'")

        routers_element = self.root.find('Routers')
        if routers_element is not None:
            for router in routers_element.findall('Router'):
                if (router.get('description') == router_description or
                    router.get('name') == router_description or
                    router.get('router') == router_description):
                    self.logger.info(f"Found router: {router.attrib}")
                    return router
        self.logger.warning(f"Router with description '{router_description}' not found.")
        return None

    def find_message_server(self, message_server_id):
        self.logger.info(f"Finding message server with ID '{message_server_id}'")
        message_servers = self.root.find('MessageServers')
        if message_servers is not None:
            for msg_server in message_servers.findall('MessageServer'):
                if msg_server.get('uuid') == message_server_id:
                    self.logger.info(f"Found message server: {msg_server.attrib}")
                    return msg_server
        self.logger.warning(f"Message server with ID '{message_server_id}' not found.")
        return None

    def find_message_server_by_description(self, name, host):
        self.logger.info(f"Finding message server with name '{name}' and host '{host}'")
        message_servers = self.root.find('MessageServers')
        if message_servers is not None:
            for msg_server in message_servers.findall('MessageServer'):
                if msg_server.get('name') == name and msg_server.get('host') == host:
                    self.logger.info(f"Found message server: {msg_server.attrib}")
                    return msg_server
                elif msg_server.get('name') == name:
                    self.logger.warning(f"Message server with name '{name}' found, but host doesn't match.")
                    continue
                elif msg_server.get('host') == host:
                    self.logger.warning(f"Message server with host '{host}' found, but name doesn't match.")
                    continue
        self.logger.warning(f"Message server with name '{name}' and host '{host}' not found.")
        return None

