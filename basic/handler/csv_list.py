import csv
import os
import typing
from basic.model_dataclasses import Person, Author, Book


def write_people(people: list[Person], path: str, file_name: str = "people.csv", delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name if file_name else "people.csv"), "w", newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerow(["id", "name", "age", "male"])
        for person in people:
            writer.writerow([person.id, person.name, person.age, person.male])


def read_people(path: str, file_name: str = "people.csv", delimiter: str = ";") -> list[Person]:
    with open(os.path.join(path, file_name if file_name else "people.csv"), "r") as file:
        reader = csv.reader(file, delimiter=delimiter)
        next(reader)
        return [Person(row[0], row[1], int(row[2]), bool(row[3])) for row in reader]


def write_authors(authors: list[Author], path: str, file_name: str = "authors.csv", delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name if file_name else "authors.csv"), "w", newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerow(["id", "name", "birth_year", "nationality"])
        for author in authors:
            writer.writerow([author.id, author.name, author.birth_year, author.nationality])


def read_authors(path: str, file_name: str = "authors.csv", delimiter: str = ";") -> list[Author]:
    with open(os.path.join(path, file_name if file_name else "authors.csv"), "r") as file:
        reader = csv.reader(file, delimiter=delimiter)
        next(reader)
        return [Author(row[0], row[1], int(row[2]), row[3]) for row in reader]


def write_books(books: list[Book], path: str, file_name: str = "books.csv", delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name if file_name else "books.csv"), "w", newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerow(["id", "title", "author_id", "year"])
        for book in books:
            writer.writerow([book.id, book.title, book.genre, book.publication_year, book.author_id, book.person_id])


def read_books(path: str, file_name: str = "books.csv", delimiter: str = ";") -> list[Book]:
    with open(os.path.join(path, file_name if file_name else "books.csv"), "r") as file:
        reader = csv.reader(file, delimiter=delimiter)
        next(reader)
        return [Book(row[0], row[1], row[2], int(row[3]), row[4], row[5]) for row in reader]


def write(entities: list[object], path: str, file_name: str = None, delimiter: str = ";") -> None:
    if isinstance(entities[0], Person):
        return write_people([typing.cast(Person, e) for e in entities], path, file_name=file_name, delimiter=delimiter)
    elif isinstance(entities[0], Author):
        return write_authors([typing.cast(Author, e) for e in entities], path, file_name=file_name, delimiter=delimiter)
    elif isinstance(entities[0], Book):
        return write_books([typing.cast(Book, e) for e in entities], path, file_name=file_name, delimiter=delimiter)
    else:
        raise RuntimeError("Unknown type of entity")


def read(entity_type: typing.Type[object], path: str, file_name: str = None, delimiter: str = ";") -> list[object]:
    if entity_type == Person:
        return read_people(path, file_name=file_name, delimiter=delimiter)
    elif entity_type == Author:
        return read_authors(path, file_name=file_name, delimiter=delimiter)
    elif entity_type == Book:
        return read_books(path, file_name=file_name, delimiter=delimiter)
    else:
        raise RuntimeError("Unknown type of entity")
