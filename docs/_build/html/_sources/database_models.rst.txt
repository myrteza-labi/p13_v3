Structure de la base de données et modèles
==========================================

Le projet utilise SQLite avec les modèles suivants :

- **Address** (`lettings.models.Address`)  
  - number (IntegerField)  
  - street (CharField)  
  - city (CharField)  
  - state (CharField)  
  - zip_code (IntegerField)  
  - country_iso_code (CharField)

- **Letting** (`lettings.models.Letting`)  
  - title (CharField)  
  - address (ForeignKey -> Address)

- **Profile** (`profiles.models.Profile`)  
  - user (ForeignKey -> auth.User)  
  - favorite_city (CharField)

Pour plus de détails, voir les fichiers de modèles :

- `lettings/models.rst`  
- `profiles/models.rst`
