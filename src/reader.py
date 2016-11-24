from urllib import request


class Reader(object):
    link = "https://polish.wunderground.com/history/airport/EPWA/"\
            "{}/DailyHistory.html?req_city={}&req_statename={}&format=1"

    def __init__(self):
        self.page = bytes()

    def get_webpage(self, date: str, country: str, city: str) -> str:
        link = self.__class__.link.format(date, country, city)
        with request.urlopen(link) as url:
            self.page = url.read()
        return self.page

    def append_file(self, file_name="out.csv"):
        with open(file_name, 'a') as out:
            if self.page:
                out.write(self.page.decode("utf-8"))
                out.write("\n\n\n")

if __name__ == '__main__':
    n = Reader()
    n.get_webpage("2016/11/05", "Poland", "Warsaw")
    print(n.page)
    n.append_file(file_name="out2.csv")