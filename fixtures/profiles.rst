profiles.json
=============

Le fichier `profiles.json` contient des informations sur les profils des utilisateurs, notamment leur utilisateur associé et leur ville préférée. Les données sont structurées sous forme de modèles JSON.

Exemple de contenu du fichier `profiles.json` :

.. code-block:: json

    [
      {
        "model": "profiles.profile",
        "pk": 1,
        "fields": {
          "user": 5,
          "favorite_city": "Buenos Aires"
        }
      },
      {
        "model": "profiles.profile",
        "pk": 2,
        "fields": {
          "user": 4,
          "favorite_city": "Barcelona"
        }
      },
      {
        "model": "profiles.profile",
        "pk": 3,
        "fields": {
          "user": 3,
          "favorite_city": "Budapest"
        }
      },
      {
        "model": "profiles.profile",
        "pk": 4,
        "fields": {
          "user": 2,
          "favorite_city": "Berlin"
        }
      }
    ]

Détails des champs :
--------------------

- **model** : Définit le modèle auquel les données se rapportent, ici `profiles.profile`.
- **pk** : La clé primaire du profil.
- **fields** : Contient les informations spécifiques à chaque profil :
  - **user** : L'ID de l'utilisateur auquel le profil est associé.
  - **favorite_city** : La ville préférée de l'utilisateur, sous forme de chaîne de caractères.

Les profils listés sont associés à des utilisateurs spécifiques, et chaque profil contient la ville préférée de l'utilisateur.
