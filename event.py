from datetime import datetime
from typing import Any, List, Literal, Optional, Union
from pydantic import BaseModel, TypeAdapter


class MyBase(BaseModel, extra="forbid"):
    pass


class Base(MyBase):
    t: Literal["event"]
    r: str
    e: str
    id: int


class PingAttr(MyBase):
    id: int
    lastannounced: Optional[datetime] = None
    lastseen: datetime
    manufacturername: str
    modelid: str
    name: str
    swversion: str
    type: str
    uniqueid: str
    productid: Optional[str] = None
    colorcapabilities: Optional[int] = None
    ctmax: Optional[int] = None
    ctmin: Optional[int] = None
    swconfigid: Optional[str] = None


class Ping(Base):
    attr: PingAttr
    uniqueid: str


class LightBase(Base):
    r: Literal["lights"]
    e: Literal["added", "changed"]
    uniqueid: str


class LightState(MyBase):
    alert: str
    on: bool
    reachable: bool
    bri: Optional[int] = None
    colormode: Optional[str] = None
    ct: Optional[int] = None
    effect: Optional[str] = None
    sat: Optional[int] = None
    xy: Optional[List[int]] = None
    hue: Optional[int] = None


class LightStateChange(LightBase):
    state: LightState


class LightStartupConfig(MyBase):
    bri: Any
    color: Any
    on: Any
    groups: Optional[List] = None


class LightConfig(LightBase):
    config: LightStartupConfig


class LightCapabilities(MyBase):
    alerts: List[str]
    bri: Any
    color: Any


class LightAddDump(MyBase):
    capabilities: LightCapabilities
    colorcapabilities: int
    config: LightStartupConfig
    ctmax: int
    ctmin: int
    etag: str
    hascolor: bool
    lastannounced: Optional[datetime] = None
    lastseen: datetime
    manufacturername: str
    modelid: str
    name: str
    productid: Optional[str] = None
    state: LightState
    swconfigid: Optional[str] = None
    swversion: Optional[str] = None
    type: str
    uniqueid: str


class LightAdded(LightBase):
    light: LightAddDump


class SensorBase(Base):
    r: Literal["sensors"]
    e: Literal["changed"]
    uniqueid: str


class SensorNameChange(SensorBase):
    name: str


class ButtonState(MyBase):
    buttonevent: int
    lastupdated: datetime


class SensorButton(SensorBase):
    state: ButtonState


class SensorButtonConfig(MyBase):
    clickmode: str
    devicemode: str
    on: bool
    reachable: bool


class ButtonConfig(SensorBase):
    config: SensorButtonConfig


class SensorBatteryConfig(MyBase):
    alert: str = None
    battery: int
    on: bool
    reachable: bool
    offset: int = None


class SensorBattery(SensorBase):
    config: SensorBatteryConfig


class TempSensorState(MyBase):
    temperature: int
    lastupdated: datetime


class HumiditySensorState(MyBase):
    humidity: int
    lastupdated: datetime


class TempHumiditySensor(SensorBase):
    state: Union[TempSensorState, HumiditySensorState]


class DaylightSensorState(MyBase):
    dark: bool
    daylight: bool
    status: int
    sunrise: datetime
    sunset: datetime
    lastupdated: datetime


class DaylightSensor(SensorBase):
    state: DaylightSensorState


class GroupState(MyBase):
    all_on: bool
    any_on: bool


class GroupStateChange(Base):
    r: Literal["groups"]
    e: Literal["changed"]
    state: GroupState


Event = TypeAdapter(
    Union[
        SensorNameChange,
        SensorButton,
        TempHumiditySensor,
        SensorBattery,
        Ping,
        LightConfig,
        LightAdded,
        ButtonConfig,
        DaylightSensor,
        LightStateChange,
        GroupStateChange,
    ]
)
