import abc

from typing import Dict, Any

from random import randint, choice
from datetime import datetime


class AbstractSensor(abc.ABC):
    def __init__(self, getter: callable):
        self.data_getter = getter

    @abc.abstractmethod
    async def get_payload(self) -> int:
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__


class Sensor(AbstractSensor):
    def __init__(self, getter: callable):
        super().__init__(getter)

    async def get_payload(self) -> int:
        return 1


class RandomSensor(AbstractSensor):
    def __init__(self, getter: callable):
        super().__init__(getter)

    async def get_payload(self, ) -> int:
        return self.data_getter(0, 20)


class TimeSensor(AbstractSensor):
    def __init__(self, getter: callable):
        super().__init__(getter)

    async def get_payload(self) -> int:
        return self.data_getter().hour % 12


class TemperatureSensor(AbstractSensor):
    def __init__(self, getter: callable):
        super().__init__(getter)

    async def get_payload(self) -> int:
        return int(abs(self.data_getter()['temp']) - 15)


class HumiditySensor(AbstractSensor):
    def __init__(self, getter: callable):
        super().__init__(getter)

    async def get_payload(self) -> int:
        return int(self.data_getter()['humidity']) % 10


class ConditionSensor(AbstractSensor):
    def __init__(self, getter: callable):
        super().__init__(getter)

    async def get_payload(self) -> int:
        conditions = ['clear', 'partly-cloudy', 'cloudy', 'overcast', 'drizzle', 'light-rain', 'rain', 'moderate-rain',
                      'heavy-rain', 'continuous-heavy-rain', 'showers', 'wet-snow', 'light-snow', 'snow',
                      'snow-showers',
                      'hail', 'thunderstorm', 'thunderstorm-with-rain', 'thunderstorm-with-hail']

        return conditions.index(self.data_getter()['condition'])


class PopulationSensor(AbstractSensor):
    def __init__(self, getter: callable):
        super().__init__(getter)

    async def get_payload(self) -> int:
        return self.data_getter() % 100000


class SeasonSensor(AbstractSensor):
    def __init__(self, getter: callable):
        super().__init__(getter)

    async def get_payload(self) -> int:
        seasons = {'winter': 3, 'spring': 1, 'summer': 0, 'autumn': 2}

        return seasons[self.data_getter()['season']]


def weather_getter() -> Dict[str, Any]:
    data = {
        'temp': randint(-20, 20),
        'humidity': randint(0, 100),
        'condition': choice(
            ['clear', 'partly-cloudy', 'cloudy', 'overcast', 'drizzle', 'light-rain', 'rain', 'moderate-rain',
             'heavy-rain', 'continuous-heavy-rain', 'showers', 'wet-snow', 'light-snow', 'snow', 'snow-showers',
             'hail', 'thunderstorm', 'thunderstorm-with-rain', 'thunderstorm-with-hail']),
        'season': choice(['winter', 'spring', 'summer', 'autumn'])
    }

    return data


def population_getter() -> int:
    return randint(1000, 10000000)


class SensorFactory:
    @staticmethod
    def get_sensor(sensor_type: str, settings) -> AbstractSensor:
        if sensor_type == 'common':
            return Sensor(None)
        elif sensor_type == 'random':
            return RandomSensor(randint)
        elif sensor_type == 'time':
            return TimeSensor(datetime.now)
        elif sensor_type == 'temperature':
            return TemperatureSensor(weather_getter)
        elif sensor_type == 'humidity':
            return HumiditySensor(weather_getter)
        elif sensor_type == 'condition':
            return ConditionSensor(weather_getter)
        elif sensor_type == 'population':
            return PopulationSensor(population_getter)
        elif sensor_type == 'season':
            return SeasonSensor(weather_getter)
        else:
            raise ValueError('Unknown sensor type')
