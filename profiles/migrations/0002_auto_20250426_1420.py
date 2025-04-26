from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='profile',
            table='oc_lettings_site_profile',
        ),
    ]
