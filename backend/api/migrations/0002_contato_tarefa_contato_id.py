# Generated by Django 4.1.1 on 2022-09-10 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contato",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=50)),
                ("data_alteracao", models.DateTimeField(auto_now=True)),
                ("data_cadastro", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name="tarefa",
            name="contato_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="api.contato",
            ),
        ),
    ]
