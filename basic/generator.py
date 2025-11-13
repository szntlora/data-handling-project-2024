import random

from faker import Faker

from basic.model_dataclasses import Person, Author, Book


def generate_people(n: int, male_ratio: float = 0.5, locale: str = "hu_HU",
                    unique: bool = False, min_age: int = 6, max_age: int = 100) -> list[Person]:
    assert n > 0
    assert 0 < male_ratio < 1
    assert 0 <= min_age <= max_age

    fake = Faker(locale)
    people = []
    for i in range(n):
        male = random.random() < male_ratio
        generator = fake if not unique else fake.unique
        people.append(Person(
            "O-" + (str(i).zfill(6)),
            generator.name_male() if male else generator.name_female(),
            random.randint(min_age, max_age),
            male))

    return people


def generate_authors(n: int, locale: str = "hu_HU", unique: bool = False, min_birth_year: int = 1800,
                     max_birth_year: int = 2010) -> list[Author]:
    assert n > 0
    assert min_birth_year <= max_birth_year

    authors = []
    fake = Faker(locale)
    fake = fake if not unique else fake.unique

    for i in range(n):
        authors.append(Author(
            id="A-" + (str(i).zfill(6)),
            name=fake.name(),
            birth_year=random.randint(min_birth_year, max_birth_year),
            nationality=fake.country()
        ))

    return authors


def generate_books(n: int, authors: list[Author],
                   people: list[Person],
                   locale: str = "hu_HU",
                   unique: bool = False,
                   borrow_probability: float = 0.5) -> list[Book]:
    assert n > 0
    assert len(authors) > 0
    assert len(people) > 0
    assert 0 <= borrow_probability <= 1

    books = []
    fake = Faker(locale)
    fake = fake if not unique else fake.unique

    for i in range(n):
        author = random.choice(authors)

        if random.random() < borrow_probability:
            person = random.choice(people)
            person_id = person.id
        else:
            person_id = None

        books.append(Book(
            id="B-" + (str(i).zfill(6)),
            title=fake.sentence(nb_words=3),
            genre=random.choice(['Sci-fi', 'Ifjúsági', 'Horror', 'Romantikus', 'Novella', 'Fantasy']),
            publication_year=random.randint(1900, 2024),
            author_id=author.id,
            person_id=person_id
        ))

    return books
