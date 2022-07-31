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
    
    def insert(self, media):
        """insert a media into database

        Args:
            media: an object of table media
        """        
        if media is not None:
            self.session.add(media)
            self.session.commit()

    def update(self, media):
        """insert a media into database

        Args:
            media: an object of table media
        """        
        if media is not None:
            self.session.commit()

    def delete(self, media):
        """insert a media into database

        Args:
            media: an object of table media
        """        
        if media is not None:
            self.session.delete(media)
            self.session.commit()

    def get(self):
        """get a record from media table

        Returns:
            ret: an object of Class/table media
        """        
        ret = self.session.query(Media).first()
        return ret

    def convert_metainfo_to_json(self, json_string):
        metainfo_json = json.loads(json_string)

        return metainfo_json

    
    def get_video_by_id(self, id):
        """get a record by id from media table

        Returns:
            ret: an object of Class/table media
        """     
        ret = self.session.query(Media).filter(Media.id == id).first()
        return ret
