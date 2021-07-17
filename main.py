"""
Задача:
Создать классы для трех видов апартаментов.
Квартира с балконом, квартира без балкона,
частный дом, дом с бассейном, при этом у всех
апартаментов есть свой конкретный адрес.
В любые  апартаменты можно зайти и можно
выйти. Так же их можно открывать и закрывать.
К тому же у частных домов может быть в
наличии гараж. Реализовать данную программу
используя принципы S, O.

Задание 1:
Создать классы для проводных наушников и блютуз наушников,
которые будут реализовывать один и тот же интерфейс взаимодействия
с пользователем и его устройствами. Создать класс пользователя,
который будет хранить в себе указатель на интерфейс наушников и
у которого должна быть возможность поменять их в любой момент
работы. При реализации классов должны быть оповещения о
производимых действиях с наушниками. Руководствоваться принципом L.

Задание 2:
К заданию выше добавить классы гарнитуры и блютуз колонок. Гарнитура
включает в себя функции микрофона, а блютуз колонка - навигацию по
аудиозаписям и настройку эквалайзера. Руководствоваться принципом I.
"""
# Задача ---------------------------------------------------------------------------------------------------------------
from abc import *


class ILocked(ABC):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass


class IVisit(ABC):

    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def leave(self):
        pass


class IApartment(ABC):

    @abstractmethod
    def address(self):
        pass

    @abstractmethod
    def balcony(self):
        pass


class IHouse(ABC):

    @abstractmethod
    def pool(self):
        pass

    @abstractmethod
    def garage(self):
        pass


class LockedLodging(ILocked):

    def __init__(self):
        self.locked = True

    def open(self):
        self.locked = False

    def close(self):
        self.locked = True


class VisitLodging(IVisit):

    def __init__(self):
        self.visit = False

    def enter(self):
        self.visit = True

    def leave(self):
        self.visit = False


class Apartment(LockedLodging, VisitLodging, IApartment):

    def __init__(self, address: str, balcony: bool):
        super().__init__()
        self._address = address
        self.balcony = balcony

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def balcony(self):
        return self._balcony

    @balcony.setter
    def balcony(self, value: bool):
        self._balcony = value


class House(LockedLodging, VisitLodging):
    def __init__(self, address: str, pool: bool, garage=True):
        super().__init__()
        self.pool = pool
        self.address = address
        self.garage = garage

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def pool(self):
        return self._pool

    @pool.setter
    def pool(self, value: bool):
        self._pool = value

    @property
    def garage(self):
        return self._address

    @garage.setter
    def garage(self, value):
        self._address = value


apartment = Apartment("Одесса, Черняховского 14", True)
apartment.open()
print(apartment.locked)
apartment.enter()
print(apartment.visit)
apartment.close()
print(apartment.locked)

# Задание 1 ------------------------------------------------------------------------------------------------------------
