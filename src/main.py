from src.parsers.parsers import Parsers

if __name__ == "__main__":
    parsers = Parsers()
    parser = parsers.get_parser("FM1110")
    print(parser.parse())
    parser2 = parsers.get_parser("GV65")
    print(parser2.parse())
