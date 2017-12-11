from pymongo import MongoClient
import argparse
import json


def run(datafile):
    data = json.load(open(datafile))
    client = MongoClient()
    db = client.final
    recipes = db.recipes
    recipes.insert_many(data)
    print("recipe JSON successfully loaded!")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='load recipe data into mogodb')

    parser.add_argument('--datafile', default="../data/epicurious-recipes/full_format_recipes.json",
                        help='recipes JSON file')

    args = parser.parse_args()
    run(args.datafile)
