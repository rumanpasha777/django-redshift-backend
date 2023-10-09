from enum import Enum


class AppEnum(Enum):

    @classmethod
    def values(cls):
        return list((i.value, i.name) for i in cls)

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)

    @classmethod
    def has_value(cls, item):
        return item in [v.value for v in cls.__members__.values()]
