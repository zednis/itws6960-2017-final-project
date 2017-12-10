from pymongo import MongoClient
import re
import pandas


class RecipeData:

    def __init__(self, host='localhost', port=27017, db="final", collection="recipes"):
        self.client = MongoClient(host, port)
        self.db = self.client[db]
        self.collection = self.db[collection]

    def is_connected(self):
        return True if self.client else None

    class RecipeQuery:

        def __init__(self, recipes):
            self.recipes = recipes
            self.query = {}

        def title_contains(self, text):
            self.query.update({"title": re.compile(text, re.IGNORECASE)})
            return self

        def description_contains(self, text):
            self.query.update({"desc": re.compile(text, re.IGNORECASE)})
            return self

        def category(self, category):
            self.query.update({"categories": re.compile(category, re.IGNORECASE)})
            return self

        def category_any_of(self, categories):
            self.query.update({"$or": [{"categories": re.compile(x, re.IGNORECASE)} for x in categories]})
            return self

        def category_all_of(self, categories):
            self.query.update({"categories": {"$all": [re.compile(x, re.IGNORECASE) for x in categories]}})
            return self

        def ingredient(self, ingredient):
            self.query.update({"ingredients": re.compile(ingredient, re.IGNORECASE)})
            return self

        def ingredient_any_of(self, ingredents):
            self.query.update({"$or": [{"ingredients": re.compile(x, re.IGNORECASE)} for x in ingredients]})
            return self

        def ingredient_all_of(self, ingredients):
            self.query.update({"ingredients": {"$all": [re.compile(x, re.IGNORECASE) for x in ingredients]}})
            return self

        def max_calories(self, max_calories):
            self.query.update({"calories": {"$lte": max_calories}})
            return self

        def max_fat(self, max_fat):
            self.query.update({"fat": {"$lte": max_fat}})
            return self

        def max_sugar(self, max_sugar):
            self.query.update({"sugar": {"$lte": max_sugar}})
            return self

        def min_protein(self, min_protein):
            self.query.update({"fat": {"$gte": min_protein}})
            return self

        def min_rating(self, min_rating):
            self.query.update({"rating": {"$gte": min_rating}})
            return self

        def run(self):
            return pandas.DataFrame(list(self.recipes.collection.find(self.query)))

        def show(self):
            return self.query

    def query(self):
        return self.RecipeQuery(self)
