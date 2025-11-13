import json
import os
from typing import cast, Type
from basic.model_dataclasses import Person, Author, Book


def write_people(people: list[Person], path: str,
                 file_name: str = "people",
                 extension: str = ".json",
                 pretty: bool = True) -> None:
    with open(os.path.join(path, file_name + extension), "w") as file:
        json.dump(
            [person.__dict__ for person in people],
            file, indent=2 if pretty else None)


def read_people(path: str, file_name: str = "people",
                extension: str = ".json") -> list[Person]:
    with open(os.path.join(path, file_name + extension)) as file:
        return json.load(file, object_hook=lambda d: Person(**d))


def write_authors(authors: list[Author], path: str, file_name: str = "authors", extension: str = ".json",
                  pretty=True) -> None:
    with open(os.path.join(path, file_name + extension), "w") as file:
        json.dump([author.__dict__ for author in authors], file, indent=2 if pretty else None)


def read_authors(path: str, file_name: str = "authors", extension: str = ".json") -> list[Author]:
    with open(os.path.join(path, file_name + extension)) as file:
        return [Author(**doc) for doc in json.load(file)]


def write_books(books: list[Book], path: str, file_name: str = "books", extension: str = ".json", pretty=True) -> None:
    with open(os.path.join(path, file_name + extension), "w") as file:
        json.dump([book.__dict__ for book in books], file, indent=2 if pretty else None)


def read_books(path: str, file_name: str = "books", extension: str = ".json") -> list[Book]:
    with open(os.path.join(path, file_name + extension)) as file:
        return [Book(**doc) for doc in json.load(file)]


def write(entities: list[object], path, file_name: str = None, extension: str = None, pretty=True) -> None:
    if isinstance(entities[0], Author):
        return write_authors([cast(Author, e) for e in entities],
                             path, file_name=file_name,
                             extension=extension, pretty=pretty)
    elif isinstance(entities[0], Book):
        return write_books([cast(Book, e) for e in entities],
                           path, file_name=file_name,
                           extension=extension, pretty=pretty)
    elif isinstance(entities[0], Person):
        return write_people([cast(Person, e) for e in entities],
                            path, file_name=file_name,
                            extension=extension, pretty=pretty)
    else:
        raise RuntimeError("Unknown type of entity")


def read(entity_type: Type[object], path, file_name: str = None, extension: str = None) -> list[object]:
    if entity_type == Author:
        return read_authors(path, file_name=file_name, extension=extension)
    elif entity_type == Book:
        return read_books(path, file_name=file_name, extension=extension)
    elif entity_type == Person:
        return read_people(path, file_name=file_name, extension=extension)
    else:
        raise RuntimeError("Unknown type of entity")
