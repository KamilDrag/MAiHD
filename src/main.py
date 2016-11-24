from date_gen import DateGen
from reader import Reader


class Main(object):
    @staticmethod
    def get_data(date_range: DateGen, places: dict):
        reader = Reader()
        for date in date_range:
            for country, cities in places.items():
                for city in cities:
                    reader.get_webpage(date, country, city)
                    reader.append_file("output.csv")


if __name__ == '__main__':
    date_gen = DateGen("2016-09-29", DateGen.today())
    locations = {
        "Poland": ["Warsaw"]
    }

    app = Main()
    app.get_data(date_gen, locations)


