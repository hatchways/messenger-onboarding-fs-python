# Generated by Django 3.2.4 on 2021-07-09 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Conversation",
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
                ("createdAt", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="User",
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
                ("username", models.TextField(unique=True)),
                ("email", models.TextField(unique=True)),
                ("photoUrl", models.TextField()),
                ("password", models.TextField()),
                ("salt", models.TextField()),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                ("firstName", models.TextField()),
                ("lastName", models.TextField()),
                ("country", models.TextField()),
                ("bio", models.TextField()),
                ("receiveNotifications", models.BooleanField()),
                ("receiveUpdates", models.BooleanField()),
                ("completedOnboarding", models.BooleanField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Message",
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
                ("text", models.TextField()),
                ("senderId", models.IntegerField()),
                ("createdAt", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                (
                    "conversation",
                    models.ForeignKey(
                        db_column="conversationId",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="messages",
                        related_query_name="message",
                        to="messenger_backend.conversation",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="conversation",
            name="user1",
            field=models.ForeignKey(
                db_column="user1Id",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="messenger_backend.user",
            ),
        ),
        migrations.AddField(
            model_name="conversation",
            name="user2",
            field=models.ForeignKey(
                db_column="user2Id",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="messenger_backend.user",
            ),
        ),
    ]
