Tests et couverture
===================

La suite de tests s’appuie sur **pytest** et **pytest-django** :

.. code-block:: bash

    # Exécuter tous les tests
    pytest

    # Générer un rapport de couverture HTML
    coverage run -m pytest
    coverage html

Le rapport se trouve ensuite dans `htmlcov/index.html`.  
La couverture de code doit être supérieure à 90%.

Astuce : pour tester un seul module :

.. code-block:: bash

    pytest path/to/module.py
