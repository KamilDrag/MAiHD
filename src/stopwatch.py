from time import clock


class Stopwatch(object):
    def __init__(self):
        self.__start_time = None
        self.__stop_time = None

    def start(self):
        self.__start_time = clock()

    def stop(self):
        self.__stop_time = (clock() - self.__start_time)

    def get_elapsed(self):
        return self.__stop_time

    def get_elapsed_int(self):
        return int(round(self.__stop_time))

if __name__ == '__main__':
    stopwatch = Stopwatch()
    from time import sleep
    print("start")
    stopwatch.start()
    sleep(2)
    print("stop")
    stopwatch.stop()
    print("seconds elapsed:" + str(stopwatch.get_elapsed()))
    print(stopwatch.get_elapsed_int())