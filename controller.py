import json
from model import *
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

class Controller:
    def __init__(self) -> None:
        self.session = None

    def connect(self, sqlite_filepath):
        engine = create_engine(f"sqlite:///{sqlite_filepath}")
        Session = sessionmaker()
        Session.configure(bind=engine, future=True)
        self.session = Session()
    
    def save(self, media):
        if media is not None:
            self.session.add(media)

    def get(self):
        ret = self.session.query(Media).first()
        return ret

    def convert_metainfo_to_json(self, json_string):
        metainfo_json = json.loads(json_string)

        return metainfo_json
