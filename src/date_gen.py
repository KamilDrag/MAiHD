from datetime import timedelta, datetime


class DateGen:
    def __init__(self, date_start: str, date_end: str):
        self.current = datetime.strptime(date_start, "%Y-%m-%d")
        self.high = datetime.strptime(date_end, "%Y-%m-%d")

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += timedelta(days=1)
            return DateGen.format_date(self.current - timedelta(days=1))

    @staticmethod
    def format_date(date: datetime) -> str:
        return date.strftime('%Y/%m/%d')

    @staticmethod
    def today() -> str:
        return datetime.now().strftime('%Y-%m-%d')

