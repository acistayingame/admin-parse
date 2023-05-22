# Generated by Django 4.2.1 on 2023-05-22 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "vendor_code",
                    models.PositiveIntegerField(
                        primary_key=True, serialize=False, verbose_name="Артикул"
                    ),
                ),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2, max_digits=15, verbose_name="Цена"
                    ),
                ),
                (
                    "cost_final",
                    models.DecimalField(
                        decimal_places=2, max_digits=15, verbose_name="Цена после СПП"
                    ),
                ),
                ("personal_sale", models.IntegerField(verbose_name="СПП")),
                (
                    "last_update",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Время обновления"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Keyword",
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
                ("value", models.CharField(verbose_name="Ключевая фраза")),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="parser.item",
                        verbose_name="Товар",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Position",
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
                (
                    "value",
                    models.IntegerField(null=True, verbose_name="Позиция в выдаче"),
                ),
                (
                    "parse_time",
                    models.DateTimeField(auto_now=True, verbose_name="Время парсинга"),
                ),
                (
                    "keyword",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="parser.keyword",
                        verbose_name="Ключевая фраза",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]