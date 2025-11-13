from typing import List
import oracledb
from basic.model_dataclasses import Person, Author, Book


def connect_to_oracle(user: str, password: str, host: str, port: int, service_name: str) -> oracledb.Connection:
    dsn = f"{host}:{port}/{service_name}"
    connection = oracledb.connect(user=user, password=password, dsn=dsn)
    print("Connected to Oracle Database using oracledb")
    return connection


def create_tables(connection: oracledb.Connection):
    cursor = connection.cursor()

    table_names = ["Book", "Author", "Person"]
    for table_name in table_names:
        try:
            cursor.execute(f"DROP TABLE {table_name}")
            print(f"Table {table_name} dropped.")
        except oracledb.DatabaseError as e:
            error_obj, = e.args
            if error_obj.code == 942:
                print(f"Table {table_name} does not exist, skipping drop.")
            else:
                raise

    cursor.execute("""
    CREATE TABLE Person (
        id VARCHAR2(50) PRIMARY KEY,
        name VARCHAR2(100),
        age NUMBER,
        male CHAR(1)
    )""")
    print("Table Person created.")

    cursor.execute("""
    CREATE TABLE Author (
        id VARCHAR2(50) PRIMARY KEY,
        name VARCHAR2(100),
        birth_year NUMBER,
        nationality VARCHAR2(100)
    )""")
    print("Table Author created.")

    cursor.execute("""
    CREATE TABLE Book (
        id VARCHAR2(50) PRIMARY KEY,
        title VARCHAR2(100),
        genre VARCHAR2(100),
        publication_year NUMBER,
        author_id VARCHAR2(50),
        person_id VARCHAR2(50), 
        CONSTRAINT fk_author FOREIGN KEY (author_id) REFERENCES Author(id),
        CONSTRAINT fk_person FOREIGN KEY (person_id) REFERENCES Person(id)
    )""")
    print("Table Book created.")

    cursor.close()
    connection.commit()


def insert_persons(connection: oracledb.Connection, persons: List[Person]):
    cursor = connection.cursor()
    for person in persons:
        cursor.execute("""
        INSERT INTO Person (id, name, age, male) VALUES (:1, :2, :3, :4)
        """, (person.id, person.name, person.age, 'M' if person.male else 'F'))
    print("Inserted persons into Person table.")
    cursor.close()
    connection.commit()


def insert_authors(connection: oracledb.Connection, authors: List[Author]):
    cursor = connection.cursor()
    for author in authors:
        cursor.execute("""
        INSERT INTO Author (id, name, birth_year, nationality) VALUES (:1, :2, :3, :4)
        """, (author.id, author.name, author.birth_year, author.nationality))
    print("Inserted authors into Author table.")
    cursor.close()
    connection.commit()


def insert_books(connection: oracledb.Connection, books: List[Book]):
    cursor = connection.cursor()
    for book in books:
        cursor.execute("""
        INSERT INTO Book (id, title, genre, publication_year, author_id) VALUES (:1, :2, :3, :4, :5)
        """, (book.id, book.title, book.genre, book.publication_year, book.author_id))
    print("Inserted books into Book table.")
    cursor.close()
    connection.commit()


def fetch_persons(connection: oracledb.Connection) -> List[Person]:
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, age, male FROM Person")
    persons = [Person(row[0], row[1], row[2], row[3] == 'M') for row in cursor]
    cursor.close()
    return persons


def fetch_authors(connection: oracledb.Connection) -> List[Author]:
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, birth_year, nationality FROM Author")
    authors = [Author(row[0], row[1], row[2], row[3]) for row in cursor]
    cursor.close()
    return authors


def fetch_books(connection: oracledb.Connection) -> List[Book]:
    cursor = connection.cursor()
    cursor.execute("SELECT id, title, genre, publication_year, author_id, person_id FROM Book")
    books = [Book(row[0], row[1], row[2], row[3], row[4], row[5]) for row in cursor]
    cursor.close()
    return books
