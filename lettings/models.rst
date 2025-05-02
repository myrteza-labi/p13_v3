Lettings – Modèles
==================

Ce module définit les modèles de l’application ``lettings``.

Il contient :

- Le modèle :class:`Address`, représentant une adresse postale complète.
- Le modèle :class:`Letting`, représentant une location associée à une adresse unique.

.. automodule:: lettings.models
   :members:
   :undoc-members:
   :show-inheritance:

Détails des modèles
-------------------

**Address**
~~~~~~~~~~~

Représente une adresse postale avec les champs suivants :

- ``number`` (int) : Numéro de rue (max 9999).
- ``street`` (str) : Nom de la rue (max 64 caractères).
- ``city`` (str) : Ville (max 64 caractères).
- ``state`` (str) : Code d’état (2 lettres).
- ``zip_code`` (int) : Code postal (max 99999).
- ``country_iso_code`` (str) : Code ISO du pays (3 lettres, ex : FRA).

Le nom de la table associée est ``oc_lettings_site_address``.  
Sa représentation texte est : ``"{number} {street}"``.

**Letting**
~~~~~~~~~~~

Représente une annonce de location avec :

- ``title`` (str) : Titre de l’annonce (max 256 caractères).
- ``address`` (FK) : L’adresse associée (relation OneToOne avec Address).

Le nom de la table associée est ``oc_lettings_site_letting``.  
Sa représentation texte est le champ ``title``.
