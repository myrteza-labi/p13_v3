from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='address',
            table='oc_lettings_site_address',
        ),
        migrations.AlterModelTable(
            name='letting',
            table='oc_lettings_site_letting',
        ),
    ]
