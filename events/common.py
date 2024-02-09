from datetime import datetime
from typing import Literal, Optional
from pydantic import BaseModel


class MyBase(BaseModel, extra="forbid"):
    pass


class Base(MyBase):
    t: Literal["event"]
    id: int


class HeartbeatAttr(MyBase):
    id: int
    lastannounced: Optional[datetime]
    lastseen: datetime
    manufacturername: str
    modelid: str
    name: str
    swversion: str
    type: str
    uniqueid: str
    productid: Optional[str] = None
