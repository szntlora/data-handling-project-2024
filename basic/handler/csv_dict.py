import csv
import os
from typing import Type, List

from basic.model_dataclasses import Person, Author, Book


def write_people(people: list[Person], path: str, file_name: str = "people.csv",
                 extension: str = ".csv", heading: bool = True, delimiter: str = ";") -> None:
    file_name = file_name if file_name is not None else "people"
    extension = extension if extension is not None else ".csv"

    with open(os.path.join(path, file_name + extension), "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "age", "male"], delimiter=delimiter)
        if heading:
            writer.writeheader()
        for person in people:
            writer.writerow(person.__dict__)


def read_people(path: str, file_name: str = "people", extension: str = ".csv", delimiter: str = ";") -> list[Person]:
    file_name = file_name if file_name is not None else "people"
    extension = extension if extension is not None else ".csv"

    with open(os.path.join(path, file_name + extension), "r") as file:
        rows = csv.DictReader(file, delimiter=delimiter)
        return [Person(row["id"], row["name"], int(row["age"]), bool(row["male"])) for row in rows]


def write_authors(authors: list[Author], path: str, file_name: str = "authors", extension: str = ".csv",
                  heading: bool = True, delimiter: str = ";") -> None:
    file_name = file_name if file_name is not None else "authors"
    extension = extension if extension is not None else ".csv"

    with open(os.path.join(path, file_name + extension), "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "birth_year", "nationality"], delimiter=delimiter)
        if heading:
            writer.writeheader()
        for author in authors:
            writer.writerow(author.__dict__)


def read_authors(path: str, file_name: str = "authors", extension: str = ".csv", delimiter: str = ";") -> list[Author]:
    file_name = file_name if file_name is not None else "authors"
    extension = extension if extension is not None else ".csv"

    with open(os.path.join(path, file_name + extension), "r") as file:
        rows = csv.DictReader(file, delimiter=delimiter)
        return [Author(row["id"], row["name"], int(row["birth_year"]), row["nationality"]) for row in rows]


def write_books(books: list[Book], path: str, file_name: str = "books", extension: str = ".csv",
                heading: bool = True, delimiter: str = ";") -> None:
    file_name = file_name if file_name is not None else "books"
    extension = extension if extension is not None else ".csv"

    with open(os.path.join(path, file_name + extension), "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "title", "genre", "publication_year", "author_id", "person_id"],
                                delimiter=delimiter)
        if heading:
            writer.writeheader()
        for book in books:
            writer.writerow(book.__dict__)


def read_books(path: str, file_name: str = "books", extension: str = ".csv", delimiter: str = ";") -> list[Book]:
    file_name = file_name if file_name is not None else "books"
    extension = extension if extension is not None else ".csv"

    with open(os.path.join(path, file_name + extension), "r") as file:
        rows = csv.DictReader(file, delimiter=delimiter)
        return [Book(row["id"], row["title"], row["genre"], int(row["publication_year"]),
                     row["author_id"], row["person_id"]) for row in rows]


def csv_dict_write(entities: List[object], path: str, file_name: str, delimiter: str = ";") -> None:
    if not entities:
        raise ValueError("The entities list is empty and cannot be written to CSV.")

    file_path = os.path.join(path, file_name)
    with open(file_path, "w", newline="") as file:
        if isinstance(entities[0], Person):
            writer = csv.DictWriter(file, fieldnames=["id", "name", "age", "male"], delimiter=delimiter)
            writer.writeheader()
            for entity in entities:
                writer.writerow(entity.__dict__)

        elif isinstance(entities[0], Author):
            writer = csv.DictWriter(file, fieldnames=["id", "name", "birth_year", "nationality"], delimiter=delimiter)
            writer.writeheader()
            for entity in entities:
                writer.writerow(entity.__dict__)

        elif isinstance(entities[0], Book):
            writer = csv.DictWriter(file,
                                    fieldnames=["id", "title", "genre", "publication_year", "author_id", "person_id"],
                                    delimiter=delimiter)
            writer.writeheader()
            for entity in entities:
                writer.writerow(entity.__dict__)

        else:
            raise RuntimeError("Unknown type of entity")


def csv_dict_read(entity_type: Type[object], path: str, file_name: str, delimiter: str = ";") -> List[object]:
    file_path = os.path.join(path, file_name)
    with open(file_path, "r") as file:
        reader = csv.DictReader(file, delimiter=delimiter)

        if entity_type == Person:
            return [Person(row["id"], row["name"], int(row["age"]), row["male"] == "True") for row in reader]
        elif entity_type == Author:
            return [Author(row["id"], row["name"], int(row["birth_year"]), row["nationality"]) for row in reader]
        elif entity_type == Book:
            return [Book(row["id"], row["title"], row["genre"], int(row["publication_year"]),
                         row["author_id"], row["person_id"]) for row in reader]
        else:
            raise RuntimeError("Unknown entity type")
