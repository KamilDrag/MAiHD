from urllib import request


class Reader(object):
    link = "https://polish.wunderground.com/history/airport/EPWA/" \
           "{}/DailyHistory.html?req_city={}&req_statename={}&format=1"

    csv_header = "czasCET,TemperaturaC,Punkt rosyC,Wilgotność,"\
            "Ciśnienie na poziomie morzahPa,WidzialnośćKm,Wind Direction,"\
            "Prędkość wiatruKm/h,prędkość w porywieKm/h,Opadymm,Wydarzenia,"\
            "Conditions,WindDirDegrees,DateUTC"

    def __init__(self):
        self.page = str()

    def get_webpage(self, date: str, country: str, city: str) -> str:
        link = self.__class__.link.format(date, country, city)
        with request.urlopen(link) as url:
            self.page = url.read().decode("utf-8")
            self.page = self.page.replace("<br />", "")\
                .replace(self.__class__.csv_header, "")\
                .replace("\n\n", "")
        return self.page

    def append_file(self, file_name="out.csv"):
        with open(file_name, 'a') as out:
            if self.page:
                out.write(self.page)


if __name__ == '__main__':
    n = Reader()
    n.get_webpage("2016/11/20", "Poland", "Warsaw")
    print(n.page)
    n.append_file(file_name="out2.csv")
