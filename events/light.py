from datetime import datetime
from typing import Any, List, Literal, Optional, Union
from .common import Base, MyBase, HeartbeatAttr


class LightState(MyBase):
    alert: str
    on: Optional[bool] = None
    reachable: bool
    bri: Optional[int] = None
    colormode: Optional[str] = None
    ct: Optional[int] = None
    effect: Optional[str] = None
    sat: Optional[int] = None
    xy: Optional[List[float]] = None
    hue: Optional[int] = None


class LightStartupConfig(MyBase):
    bri: Any
    color: Any
    on: Any
    groups: Optional[List] = None


class LightCapabilities(MyBase):
    alerts: List[str]
    bri: Optional[Any] = None
    color: Optional[Any] = None


class LightAddDump(MyBase):
    capabilities: LightCapabilities
    colorcapabilities: Optional[int] = None
    config: Optional[LightStartupConfig] = None
    ctmax: Optional[int] = None
    ctmin: Optional[int] = None
    etag: str
    hascolor: bool
    lastannounced: Optional[datetime]
    lastseen: datetime
    manufacturername: str
    modelid: str
    name: str
    productid: Optional[str]
    state: LightState
    swconfigid: Optional[str] = None
    swversion: Optional[str]
    type: str
    uniqueid: str


class LightAnnouncementAttr(HeartbeatAttr):
    colorcapabilities: int
    ctmax: int
    ctmin: int
    swconfigid: str


class LightBase(Base):
    r: Literal["lights"]
    uniqueid: str


class LightChanged(LightBase):
    e: Literal["changed"]
    attr: Optional[Union[HeartbeatAttr, LightAnnouncementAttr]] = None
    state: Optional[LightState] = None
    config: Optional[LightStartupConfig] = None


class LightAdded(LightBase):
    e: Literal["added"]
    light: LightAddDump
