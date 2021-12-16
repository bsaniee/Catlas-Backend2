"""Cat Model."""

from masoniteorm.models import Model


class Cat(Model):
    __table__="cats"