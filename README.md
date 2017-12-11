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

TODO
 
### Dependencies
- python3
  - psycogp2
  - sqlalchemy
  - pymongo
- jupyter
  - pandas
  - matplotlib

 
### How-to load the data

TODO

```commandline
python3 
```
 
### How to run the application

The application is a jupyter python3 notebook.  This notebook loads libraries that provide fluent APIs for querying the product and recipes datasets and includes a locally-defined class ``DistributedQuery`` which implements a fluent API that allows for federated queries against both databases.

#### Installing Jupyter

jupyter should be installed by running
```commandline
python3 -m pip install -r requirements.txt
```

from the app directory

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
