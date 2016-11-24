from src.date_gen import DateGen
from src.reader import Reader
from src.stopwatch import Stopwatch


class Main(object):
    @staticmethod
    def get_data(date_range: DateGen, places: dict):
        reader = Reader()
        for date in date_range:
            for country, cities in places.items():
                for city in cities:
                    reader.get_webpage(date, country, city)
                    reader.append_file("warsaw.csv")


if __name__ == '__main__':
    date_gen = DateGen("2005-01-01", "2015-12-31")
    locations = {
        "Poland": ["Warsaw"]
    }

    app = Main()
    sw = Stopwatch()
    sw.start()
    app.get_data(date_gen, locations)
    sw.stop()
    print(sw.get_elapsed_int())


