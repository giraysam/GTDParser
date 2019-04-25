from src.parsers.quecklinkparser import QuecklinkParser
from src.parsers.teltonikaparser import TeltonikaParser
from src.parsers.parserfactory import ParserFactory


class Parsers:

    def __init__(self):
        self.parser = None
        self.factory = ParserFactory()
        self.factory.register("GV65", QuecklinkParser)
        self.factory.register("FM1110", TeltonikaParser)

    def get_parser(self, device_type):
        return self.factory.get_parser(device_type)
