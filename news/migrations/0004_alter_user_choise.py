# Generated by Django 5.0.2 on 2024-04-18 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_rename_role_user_choise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='choise',
            field=models.CharField(choices=[('politics', 'Politics'), ('sports', 'Sports'), ('technology', 'Technology'), ('health', 'Health'), ('entertainment', 'Entertainment'), ('weather', 'Weather'), ('business', 'Business')], max_length=100),
        ),
    ]
