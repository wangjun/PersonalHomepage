import os
import peewee
import configparser
from peewee import *

cf = configparser.ConfigParser()
cf.read('../homepage.config')
DB_PASS = cf.get('config', 'DB_PASS')


class UnknownField(object):
    def __init__(self, *_, **__):
        pass


class BaseModel(Model):
    class Meta:
        database = MySQLDatabase('my_app', user='root', password=DB_PASS, host='localhost', port=3306)


class search_engines(BaseModel):
    name = CharField()
    main_url = CharField()
    auto_complete_url = CharField()
    icon = CharField()

    class Meta:
        table_name = 'search_engines'

class search_engines_log(BaseModel):
    user_id = IntegerField()
    user = CharField()
    engine_id= IntegerField()
    search_text = CharField()
    ip = CharField()
    update_time = DateTimeField()

    class Meta:
        table_name = 'search_engines_log'

search_engines.create_table()
search_engines_log.create_table()