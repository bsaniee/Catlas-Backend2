""" A CatController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Cat import Cat


class CatController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request:Request):
        self.request = request

    def show(self):
        id = self.request.param("id")
        return Cat.where("id", id).get()

    def index(self):
        return Cat.all()

    def create(self):
        cat = self.request.only("name", "color", 'breed', 'image', 'description')
        return Cat.create(cat)

    def update(self):
        id = self.request.param("id")
        cat = self.request.only("name", "color", 'breed', 'image', 'description')
        Cat.where("id", id).update(cat)
        return Cat.where("id", id).get()

    def destroy(self):
        id = self.request.param("id")
        cat = Cat.where("id", id).get()
        Cat.where("id", id).delete()
        return cat