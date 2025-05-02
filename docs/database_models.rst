Modèles de données
==================

Cette section décrit les modèles utilisés dans le projet et leur structure.  
Chaque application Django gère ses propres modèles de manière isolée.

---

oc_lettings_site
----------------

Cette app contient la configuration centrale du projet, mais **ne définit pas de modèle de données**.  
Elle sert à la configuration des routes, du monitoring, du logging, et des pages d’erreur.

---

lettings
--------

Modèle **Address**
^^^^^^^^^^^^^^^^^^

Représente une adresse postale.

Champs :
- `number` (PositiveIntegerField) : numéro de rue (max 9999)
- `street` (CharField, max_length=64) : nom de la rue
- `city` (CharField, max_length=64) : ville
- `state` (CharField, 2 caractères) : abréviation de l’état
- `zip_code` (PositiveIntegerField) : code postal (max 99999)
- `country_iso_code` (CharField, 3 caractères) : code ISO du pays

Méthodes :
- `__str__()` : retourne une version courte de l’adresse (`123 Main Street`)

Options Meta :
- `db_table` = `oc_lettings_site_address`
- `verbose_name` = `Address`
- `verbose_name_plural` = `Addresses`

---

Modèle **Letting**
^^^^^^^^^^^^^^^^^^

Représente un logement proposé à la location.

Champs :
- `title` (CharField, max_length=256) : titre du logement
- `address` (OneToOneField vers Address, `on_delete=models.CASCADE`) : adresse associée

Méthodes :
- `__str__()` : retourne le titre du logement

Options Meta :
- `db_table` = `oc_lettings_site_letting`
- `verbose_name` = `Letting`
- `verbose_name_plural` = `Lettings`

---

profiles
--------

Modèle **Profile**
^^^^^^^^^^^^^^^^^^

Représente les informations complémentaires d’un utilisateur.

Champs :
- `user` (OneToOneField vers `auth.User`, `on_delete=models.CASCADE`) : utilisateur associé
- `favorite_city` (CharField, max_length=64, optionnel) : ville préférée

Méthodes :
- `__str__()` : retourne le nom d’utilisateur (ex. `jdoe`)

Options Meta :
- `db_table` = `oc_lettings_site_profile`
- `verbose_name` = `Profile`
- `verbose_name_plural` = `Profiles`
