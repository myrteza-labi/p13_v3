Profiles – Models
=================

Ce module définit les modèles de données pour l’application ``profiles``.

.. automodule:: profiles.models
   :members:
   :undoc-members:
   :show-inheritance:

Modèles disponibles
-------------------

**1. Profile**
~~~~~~~~~~~~~~

- **Champ `user`** : Lien ``OneToOne`` avec le modèle ``User`` de Django.  
  Cela signifie qu’un seul profil peut être associé à un utilisateur donné.

- **Champ `favorite_city`** : Une chaîne de caractères (64 caractères max), facultative (``blank=True``), représentant la ville préférée de l’utilisateur.

- **Méthode `__str__`** : Retourne le nom d’utilisateur (`username`) du profil.

- **Meta options** :
  - `db_table` : le nom explicite de la table dans SQLite sera `oc_lettings_site_profile`.
  - `verbose_name` : utilisé pour l’affichage administratif ("Profile").
  - `verbose_name_plural` : affichage pluriel ("Profiles").

Exemple d’utilisation
---------------------

Créer un profil :

.. code-block:: python

    from django.contrib.auth.models import User
    from profiles.models import Profile

    user = User.objects.create_user(username='jdoe', password='pass')
    profile = Profile.objects.create(user=user, favorite_city='Paris')

Afficher son nom d’utilisateur :

.. code-block:: python

    print(str(profile))  # Affiche : jdoe
