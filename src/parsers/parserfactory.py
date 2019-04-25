class ParserFactory:
    def __init__(self):
        self._creators = {}

    def register(self, device_type, creator):
        self._creators[device_type] = creator

    def get_parser(self, device_type):
        creator = self._creators.get(device_type)

        if not creator:
            raise ValueError(device_type)

        return creator()
