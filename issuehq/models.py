import datetime
from uuid import uuid4
from peewee import *
from issuehq.db import db
import nanoid


class Repository(Model):
    name = CharField()
    full_name = CharField()
    description = TextField(default="")
    html_url = CharField()

    class Meta:
        database = db


class Issue(Model):
    public_id = CharField(unique=True, default=nanoid.generate)
    uuid = UUIDField(unique=True, default=uuid4)
    repository = ForeignKeyField(Repository, backref="issues")
    title = CharField()
    body = TextField(default="")
    number = IntegerField()
    state = CharField()
    html_url = CharField()

    class Meta:
        database = db


class Search(Model):
    query = CharField()
    mode = CharField()
    limit = IntegerField()
    alpha = DoubleField(null=True)
    created_at = TimestampField(default=datetime.datetime.now)
    result_count = IntegerField(default=0)

    class Meta:
        database = db


db.create_tables([Repository, Issue, Search])
