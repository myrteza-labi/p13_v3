users.json
==========

Le fichier `users.json` contient des informations sur les utilisateurs du système. Chaque utilisateur est décrit par des données de connexion, des informations de profil et des permissions. Les données sont structurées sous forme de modèles JSON.

Exemple de contenu du fichier `users.json` :

.. code-block:: json

    [
      {
        "model": "auth.user",
        "pk": 1,
        "fields": {
          "password": "pbkdf2_sha256$180000$p35UH2yYInHF$4LTphT2basUmvfLq+XHETVvKONZrWUsLfKu1K8/Hqdk=",
          "last_login": "2020-06-14T09:41:56.975Z",
          "is_superuser": true,
          "username": "admin",
          "first_name": "",
          "last_name": "",
          "email": "admin@email.com",
          "is_staff": true,
          "is_active": true,
          "date_joined": "2020-06-14T09:41:15.326Z",
          "groups": [],
          "user_permissions": []
        }
      },
      {
        "model": "auth.user",
        "pk": 2,
        "fields": {
          "password": "pbkdf2_sha256$180000$8ZKjEEdeYubZ$jq4T/Vaa2DWdAvzNys4ynNO6Wd/PsWe3dux20F7BGgQ=",
          "last_login": null,
          "is_superuser": false,
          "username": "4meRomance",
          "first_name": "John",
          "last_name": "Rodriguez",
          "email": "coemperor@famemma.net",
          "is_staff": false,
          "is_active": true,
          "date_joined": "2020-06-14T09:44:05Z",
          "groups": [],
          "user_permissions": []
        }
      },
      {
        "model": "auth.user",
        "pk": 3,
        "fields": {
          "password": "pbkdf2_sha256$180000$DdNkE39rolFF$nGmWZanXv4GlcTxtfUgc+MUIqBgDszAtvFfuFu538LQ=",
          "last_login": null,
          "is_superuser": false,
          "username": "AirWow",
          "first_name": "Ada",
          "last_name": "Paul",
          "email": "flocation.vam4@glendenningflowerdesign.com",
          "is_staff": false,
          "is_active": true,
          "date_joined": "2020-06-14T09:44:45Z",
          "groups": [],
          "user_permissions": []
        }
      },
      {
        "model": "auth.user",
        "pk": 4,
        "fields": {
          "password": "pbkdf2_sha256$180000$3VJdHtu39cbD$8qNVkvJ0KddsvfFueEm09Sg0LxgFievigmtAEb39paE=",
          "last_login": null,
          "is_superuser": false,
          "username": "DavWin",
          "first_name": "Cassandra",
          "last_name": "Grahm",
          "email": "5houssam.kessaiso@facpidif.ml",
          "is_staff": false,
          "is_active": true,
          "date_joined": "2020-06-14T09:46:28Z",
          "groups": [],
          "user_permissions": []
        }
      },
      {
        "model": "auth.user",
        "pk": 5,
        "fields": {
          "password": "pbkdf2_sha256$180000$zjnQu4LiqMAT$Qxom08ahzw11iPlX6kYyySa94yJXdjrptta6Qzx8HWE=",
          "last_login": null,
          "is_superuser": false,
          "username": "HeadlinesGazer",
          "first_name": "Jamie",
          "last_name": "Lal",
          "email": "jssssss33@acee9.live",
          "is_staff": false,
          "is_active": true,
          "date_joined": "2020-06-14T09:47:21Z",
          "groups": [],
          "user_permissions": []
        }
      }
    ]

Détails des champs :
--------------------

- **model** : Définit le modèle auquel les données se rapportent, ici `auth.user`.
- **pk** : La clé primaire de l'utilisateur.
- **fields** : Contient les informations spécifiques à chaque utilisateur :
  - **password** : Le mot de passe de l'utilisateur, crypté.
  - **last_login** : La date et l'heure de la dernière connexion de l'utilisateur.
  - **is_superuser** : Indique si l'utilisateur est un superutilisateur.
  - **username** : Le nom d'utilisateur unique.
  - **first_name** : Le prénom de l'utilisateur.
  - **last_name** : Le nom de famille de l'utilisateur.
  - **email** : L'adresse email de l'utilisateur.
  - **is_staff** : Indique si l'utilisateur est membre du personnel.
  - **is_active** : Indique si le compte utilisateur est actif.
  - **date_joined** : La date et l'heure de l'inscription de l'utilisateur.
  - **groups** : Les groupes auxquels l'utilisateur appartient (ici, vide).
  - **user_permissions** : Les permissions spécifiques assignées à l'utilisateur (ici, vide).

Les utilisateurs listés ont des rôles et des permissions différents, avec des informations de connexion et de profil.
