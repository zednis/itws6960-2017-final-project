import re
import pandas
import argparse
from sqlalchemy.orm import sessionmaker

from food_fact_models import db_connect, create_all, drop_all, Product, Category, Ingredient, Label


categories = {}
ingredients = {}
products = {}
labels = {}


def get_categories(text):

    z = str(text).split(',')
    _categories = []

    for x in z:
        if x:
            if x not in categories:
                _x = Category(name=x)
                categories[x] = _x
                _categories.append(_x)
            else:
                _categories.append(categories[x])

    return _categories


def get_ingredients(text):

    z = re.split(',|\(|\)|\.|\[|\]|•|:|;', str(text))
    z = [x.strip(' ').lower() for x in z if x and x != 'None']
    z = [x.replace("org ", "organic ") for x in z]

    _ingredients = []

    for x in z:
        if x:
            if x not in ingredients:
                _x = Ingredient(name=x)
                ingredients[x] = _x
                _ingredients.append(_x)
            else:
                _ingredients.append(ingredients[x])

    return _ingredients


def get_or_create(hash, items, func):
    _new = []
    for item in items:
        if item:
            if item not in hash:
                obj = func(item)
                hash[item] = obj
                _new.append(obj)
            else:
                _new.append(hash[item])

    return _new


def get_labels(text):
    z = re.split(',', str(text))
    z = [x.strip(' ').lower() for x in z if x and x != 'None']
    return get_or_create(labels, z, lambda x: Label(name=x))


def validate_numeric_fields(fields, max_value):
    for field in fields:
        if field and float(field) > max_value:
            return False
    return True


def validate_numeric_field(field, max_value):
    return False if field and float(field) > max_value else True


def create_foodfact(row):

    categories = get_categories(row['categories_en'])
    ingredients = get_ingredients(row['ingredients_text'])
    labels = get_labels(row['labels_en'])

    if not row['code']:
        return None

    return Product(
        code=row['code'],
        url=row['url'],
        name=row['product_name'],
        categories=categories,
        brands=row['brands'],
        ingredients=ingredients,
        labels=labels,
        calories_100g=row['energy_100g'],
        calories_from_fat_100g=row['energy-from-fat_100g'],
        protein_100g=row['proteins_100g'],
        fat_100g=row['fat_100g'],
        saturated_fat_100g=row['saturated-fat_100g'],
        sugars_100g=row['sugars_100g'],
        carbohydrates_100g=row['carbohydrates_100g']
    )


def set_up():
    engine = db_connect()
    drop_all(engine)
    create_all(engine)
    return sessionmaker(bind=engine)


def persist(session_factory, items):
    session = session_factory()
    try:
        session.add_all(items)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
    return items


def run(datafile):

    _data = []
    for chunk in pandas.read_csv(datafile, delimiter='\t', chunksize=50000, low_memory=False, error_bad_lines=False):
        _data.append(chunk)

    df = pandas.concat(_data, axis=0)
    del _data

    df = df.where(pandas.notnull(df), None)

    session_factory = set_up()

    _products = []
    _codes = set()

    for row in df.iterrows():
        x = row[1]

        if x is None or "code" not in x:
            continue

        if str(x["code"]).strip() in _codes:
            continue

        numeric_fields = [
            x['energy_100g'],
            x['energy-from-fat_100g'],
            x['proteins_100g'],
            x['fat_100g'],
            x['saturated-fat_100g'],
            x['sugars_100g'],
            x['carbohydrates_100g']
        ]

        if not validate_numeric_fields(numeric_fields, 10000):
            print("invalid numeric field", x["code"], x["product_name"])
            continue

        ff = create_foodfact(x)

        if ff and ff.code:
            _products.append(ff)
            _codes.add(str(ff.code).strip())

    persist(session_factory, _products)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='load food product data into postgresql')
    parser.add_argument('--datafile', default="../../data/open-food-facts/en.openfoodfacts.org.products.csv",
                        help='open food facts CSV file')

    args = parser.parse_args()
    run(args.datafile)
