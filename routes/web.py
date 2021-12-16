"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([
        Get("/", "CatController@index").name("index"),
        Get("/@id", "CatController@show").name("index"),
        Post("/", "CatController@create").name("create"),
        Put("/@id", "CatController@update").name("update"),
        Delete("/@id", "CatController@destroy").name("destroy"),
    ], prefix="/cats", name="cats")
]
