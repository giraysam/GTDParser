from src.parsers.quecklinkparser import QuecklinkParser
from src.parsers.teltonikaparser import TeltonikaParser
from src.parsers.parserfactory import ParserFactory


class Parsers:

    def __init__(self):
        self.factory = ParserFactory()
        self.factory.register("GV65", QuecklinkParser)
        self.factory.register("FM1110", TeltonikaParser)

    def parse(self, device_type):
        parser = self.factory.get_parser(device_type)
        return parser.parse()
