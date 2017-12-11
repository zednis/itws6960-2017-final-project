# ITWS-6960 2017 Final Project

 Stephan Zednik
 
## Data
 
### Open Food Facts

Open Food Facts is a free, open, collaborative database of food products from around the world, with ingredients, allergens, nutrition facts and all the tidbits of information we can find on product labels.

Individual contents of the database are available under the Database Contents License.

Available Formats: CSV/TSV and SQLite.

Data access link: https://www.kaggle.com/openfoodfacts/world-food-facts

Dataset description: https://world.openfoodfacts.org/data/data-fields.txt

### Epicurious Recipe Dataset

Over 20k recipes listed by recipe rating, basic nutritional information, assigned category, ingredients, and cooking instructions lifted from http://www.epicurious.com/recipes-menus.

The kaggle dataset page does not appear to specify a license for the dataset publication.

Available Formats: JSON (full recipe data)

data access link: https://www.kaggle.com/hugodarwood/epirecipes
 
## Installation Instructions

### Databases

The application uses postgresql and mongodb for data persistence.

Instructions for installing postgresql are available at https://www.postgresql.org/docs/9.2/static/tutorial-install.html.

Instructions for install mongodb are available at https://docs.mongodb.com/manual/installation/.

The ``scripts/setup.sh`` script, and the data-loading scripts it calls, expect there to be local instances of postgresql and mongodb.

To change postgresql connection info modify the DATABASE object in ``scripts/food_fact_models.py``.

To change mogodb connection info modify values from the run function in ``scripts/load-recipes.py``.
 
### Python Dependencies
- python3
  - psycogp2
  - sqlalchemy
  - pymongo
- jupyter
  - pandas
  - matplotlib
  
If you have python3 installed you can install the other python dependencies by running

```commandline
python3 -m pip install -r requirements.txt
```

from both the scripts/ and app/ directories.

 
### How-to load the data

The ``scripts/load-open-food-facts.py`` and ``scripts/load-recipes.py`` scripts will load the data into a locally-running postgresql and mongodb database, respectively.

These scripts are called by ``scripts/setup.sh`` and need not be run individually.
 
### How to run the application

The application is a jupyter python3 notebook.  This notebook loads libraries that provide fluent APIs for querying the product and recipes datasets and includes a locally-defined class ``DistributedQuery`` which implements a fluent API that allows for federated queries against both databases.

#### Installing Jupyter

jupyter should be installed by running
```commandline
cd app
python3 -m pip install -r requirements.txt
```

or manually npm with command:
```commandline
python3 -m pip jupyter
```

Running jupyter is as easy as typing
```commandline
jupyter notebook
```

from the app directory.

More information on installing and running jupyter notebook can be found at http://jupyter.org/install.html.

#### Using the Jupyter notebook

After starting jupyter go to URL printed to the commandline (e.g. ``localhost:8888``) and open the app.ipynb notebook.

Instructions and examples for using the product and recipe APIs for querying data are available in the notebook.

More information about running jupyter cat be found at https://jupyter.readthedocs.io/en/latest/running.html#running.
