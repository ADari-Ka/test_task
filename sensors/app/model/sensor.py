import abc
from random import randint


class AbstractSensor(abc.ABC):
    @abc.abstractmethod
    async def get_data(self) -> int:
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__


class RandomSensor(AbstractSensor):
    async def get_data(self):
        return randint(0, 100)

