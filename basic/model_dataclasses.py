from dataclasses import dataclass, field


@dataclass
class Person:
    id: str = field(hash=True)
    name: str = field(repr=True, compare=False)
    age: int = field(repr=True, compare=False)
    male: bool = field(default=True, repr=True, compare=False)


@dataclass
class Author:
    id: str = field(hash=True)
    name: str = field(repr=True, compare=False)
    birth_year: int = field(repr=True, compare=False)
    nationality: str = field(repr=True, compare=False)


@dataclass
class Book:
    id: str = field(hash=True)
    title: str = field(repr=True, compare=False)
    genre: str = field(repr=True, compare=False)
    publication_year: int = field(repr=True, compare=False)
    author_id: str = field(compare=False)
    person_id: str = field(compare=False)
