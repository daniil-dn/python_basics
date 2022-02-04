import time


class TrafficLight:
    def __init__(self):
        self.__color = ""

    def running(self):
        colors_time = {'красный': 4, 'жёлтый': 2, "зелёный": 3}
        for k, v in colors_time.items():
            self.__color = k
            print(f"{k} {v} сек")
            time.sleep(v)


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
