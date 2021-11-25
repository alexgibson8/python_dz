import time


class TrafficLight:
    _colour = 'red'

    def running(self):
        print(self._colour)
        time.sleep(7)
        TrafficLight._colour = 'yellow'
        print(self._colour)
        time.sleep(2)
        TrafficLight._colour = 'green'
        print(self._colour)


traffic_light_1 = TrafficLight()
traffic_light_1.running()
