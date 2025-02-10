from datetime import datetime

from models.ObjavaBase import ObjavaBase


class Objava(ObjavaBase):
    id: int
    vrijeme: datetime
