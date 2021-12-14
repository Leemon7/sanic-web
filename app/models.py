# -*- coding: utf-8 -*-
# Created by: Leemon7
# Created on: 2021/11/13
# Function: 模型类
import datetime

from peewee import DateTimeField, ForeignKeyField, MySQLDatabase, Model
from peewee import CharField, PrimaryKeyField, TextField, IntegerField, FloatField

from app.settings import DATABASES

db = MySQLDatabase(**DATABASES)


class EmailSite(Model):
    id = PrimaryKeyField()
    site_id = CharField(max_length=15)
    site_type = CharField(max_length=15)
    site_name = CharField(max_length=45)
    api_url = CharField()
    special = CharField(max_length=15, default='')
    create_time = DateTimeField(default=datetime.datetime.now(), formats='%Y-%m-%d %H:%M:%S')
    update_time = DateTimeField(default=datetime.datetime.now(), formats='%Y-%m-%d %H:%M:%S')

    class Meta:
        database = db
        table_name = 'email_site'