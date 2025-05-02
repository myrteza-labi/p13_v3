CI – Tests continus (ci.yml)
============================

Ce fichier configure un pipeline de **tests automatisés** via **GitHub Actions**, déclenché à chaque :

- **push** sur n’importe quelle branche ;
- **pull request** vers n’importe quelle branche.

Il vise à assurer la qualité et la stabilité du code en exécutant automatiquement :

- L'installation des dépendances,
- Le linting avec ``flake8``,
- Les tests unitaires avec ``coverage``.

Structure du fichier
--------------------

.. code-block:: yaml

   name: Django CI
   on: [push, pull_request]

Jobs définis
------------

1. **test**

   Ce job s’exécute sur un environnement ``ubuntu-latest``. Il comprend les étapes suivantes :

   - **Checkout** du code source :
     
     .. code-block:: yaml

        - name: Checkout code
          uses: actions/checkout@v4

   - **Installation de Python 3.11** :

     .. code-block:: yaml

        - name: Set up Python
          uses: actions/setup-python@v5
          with:
            python-version: '3.11'

   - **Installation des dépendances** du projet + outils de qualité :

     .. code-block:: bash

        pip install -r requirements.txt
        pip install flake8 coverage

   - **Vérification du style de code** avec ``flake8`` :

     .. code-block:: yaml

        - name: Lint code with flake8
          run: flake8

   - **Exécution des tests unitaires** avec mesure de couverture :

     .. code-block:: yaml

        - name: Run tests with coverage
          run: |
            coverage run --source='.' manage.py test
            coverage report --omit="*/venv/*" --fail-under=80

Utilité
-------

- ✅ Empêche l'intégration de code cassé ou non conforme ;
- ✅ Assure une couverture de test minimale de **80%** ;
- ✅ Renforce la fiabilité du projet en validant automatiquement chaque contribution.
