import typing
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm.exc import DetachedInstanceError
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

video_info = {
   "bit_rate":"234798",
   "bits_per_raw_sample":"8",
   "closed_captions":0,
   "codec_long_name":"H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
   "codec_name":"h264",
   "codec_tag":"0x31637661",
   "codec_tag_string":"avc1",
   "codec_time_base":"1/48",
   "codec_type":"video",
   "coded_height":1920,
   "coded_width":1080,
   "display_aspect_ratio":"16:9",
   "disposition":{
      "attached_pic":0,
      "clean_effects":0,
      "comment":0,
      "default":1,
      "dub":0,
      "forced":0,
      "hearing_impaired":0,
      "karaoke":0,
      "lyrics":0,
      "original":0,
      "timed_thumbnails":0,
      "visual_impaired":0
   },
   "duration":"446.958333",
   "duration_ts":232960,
   "time_base":"1/12288",
}

video_url = 'https://www.youtube.com/watch?v=tMBKbyDzGD8'

class BaseModel():

    def __repr__(self) -> str:
        return self._repr(id=self.id)

    def _repr(self, **fields: typing.Dict[str, typing.Any]) -> str:
        '''
        Helper for __repr__
        '''
        field_strings = []
        at_least_one_attached_attribute = False
        for key, field in fields.items():
            try:
                field_strings.append(f'{key}={field!r}')
            except DetachedInstanceError:
                field_strings.append(f'{key}=DetachedInstanceError')
            else:
                at_least_one_attached_attribute = True
        if at_least_one_attached_attribute:
            return f"<{self.__class__.__name__}({','.join(field_strings)})>"
        return f"<{self.__class__.__name__} {id(self)}>"


class Media(Base, BaseModel):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    metainfo = Column(String)
    url = Column(String)
    type = Column(String)


    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self) -> str:
        return self._repr(id=self.id, 
                          metainfo=self.metainfo, 
                          url=self.url, 
                          type=self.type)
