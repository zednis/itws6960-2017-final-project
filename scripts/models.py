from sqlalchemy import create_engine, Column, String, Numeric, ForeignKey, Table
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': 5432,
    'username': 'foodfacts',
    'password': 'foodfacts',
    'database': 'foodfacts'
}


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**DATABASE))


def create_all(engine):
    Base.metadata.create_all(engine)


def drop_all(engine):
    Base.metadata.drop_all(engine)


product_category = Table(
    'product_category',
    Base.metadata,
    Column('product', String, ForeignKey('products.code')),
    Column('category', String, ForeignKey('categories.name'))
)

product_ingredient = Table(
    'product_ingredient',
    Base.metadata,
    Column('product', String, ForeignKey('products.code')),
    Column('ingredient', String, ForeignKey('ingredients.name'))
)


class Product(Base):
    __tablename__ = 'products'

    code = Column(String, primary_key=True)
    url = Column(String)
    name = Column(String)

    categories = relationship("Category", secondary="product_category")

    labels = relationship("Label")
    brands = Column(String)

    ingredients = relationship("Ingredient", secondary="product_ingredient")

    calories_100g = Column(Numeric)
    calories_from_fat_100g = Column(Numeric)

    protein_100g = Column(Numeric(8, 2))
    fat_100g = Column(Numeric(8, 2))
    saturated_fat_100g = Column(Numeric(8, 2))
    sugars_100g = Column(Numeric(8, 2))
    carbohydrates_100g = Column(Numeric(8, 2))

    def __repr__(self) -> str:
        return "code: {} url: {} product name: {}".format(self.code, self.url, self.product_name)


class Category(Base):
    __tablename__ = 'categories'

    name = Column(String, primary_key=True)

    def __repr__(self) -> str:
        return "name: {}".format(self.name)


class Ingredient(Base):
    __tablename__ = "ingredients"

    name = Column(String, primary_key=True)

    def __repr__(self) -> str:
        return "name: {}".format(self.name)


class Label(Base):
    __tablename__ = "labels"

    name = Column(String, primary_key=True)
    product = Column(String, ForeignKey('products.code'), primary_key=True)

    def __repr__(self) -> str:
        return "label: {}, product: {}".format(self.name, self.product)