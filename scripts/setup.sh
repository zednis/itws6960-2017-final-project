#!/bin/bash
set -ex

echo "ensuring python3 dependencies are installed"
python3 -m pip install -r requirements.txt

#echo "downloading food facts CSV to data/"
#wget -O data/en.openfoodfacts.org.products.csv http://world.openfoodfacts.org/data/en.openfoodfacts.org.products.csv

cd data
echo "unzipping product facts CSV"
unzip en.openfoodfacts.org.products.csv.zip

echo "unzipping recipes JSON"
unzip epicurious-recipes-with-rating-and-nutrition.zip

cd ..

echo "creating foodfacts user and database in local postgresql"
createuser foodfacts || true
createdb -O foodfacts foodfacts || true

echo "loading food facts data into postgresql"
echo "note - this is a very large dataset and will likely take up to 30 minutes to load"
python3 load-open-food-facts.py --datafile data/en.openfoodfacts.org.products.csv
echo "done loading food facts into postgresql!"

echo "loading recipe data in mongodb"
python3 load-recipes.py --datafile data/full_format_recipes.json
echo "done loading recipe data info mongodb"

echo "loading application python dependencies"
cd ../app
python3 -m pip install -r requirements.txt