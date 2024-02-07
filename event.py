from datetime import datetime
from typing import Literal, Optional, Union
from pydantic import BaseModel, TypeAdapter

class MyBase(BaseModel, extra='forbid'):
    pass

class Base(MyBase):
    t: Literal['event']
    id: str

class PingAttr(MyBase):
    id: int
    lastannounced: datetime
    lastseen: datetime
    manufacturername: str
    modelid: str
    name: str
    swversion: str
    type: str
    uniqueid: str
    productid: Optional[str] = None

class LightBase(Base):
    r: Literal['lights']
    e: Literal['changed']
    uniqueid: str

class LightState(MyBase):
    alert: str
    on: bool
    reachable: bool
    bri: Optional[int] = None

class LightStateChange(LightBase):
    state: LightState

class LightPing(LightBase):
    attr: PingAttr

class SensorBase(Base):
    r: Literal['sensors']
    e: Literal['changed']
    uniqueid: str

class SensorNameChange(SensorBase):
    name: str

class ButtonState(MyBase):
    buttonevent: int
    lastupdated: datetime

class SensorButtonEvent(SensorBase):
    state: ButtonState

class SensorButtonConfig(MyBase):
    clickmode: str
    devicemode: str
    on: bool
    reachable: bool

class ButtonConfig(SensorBase):
    config: SensorButtonConfig

class SensorBatteryConfig(MyBase):
    alert: str
    battery: int
    on: bool
    reachable: bool

class SensorBatteryLevel(SensorBase):
    config: SensorBatteryConfig

class TempSensorState(MyBase):
    temperature: int
    lastupdated: datetime

class HumiditySensorState(MyBase):
    humidity: int
    lastupdated: datetime

class TempHumiditySensor(SensorBase):
    state: Union[TempSensorState, HumiditySensorState]

class SensorPing(SensorBase):
    attr: PingAttr

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
    r: Literal['groups']
    e: Literal['changed']
    state: GroupState

Event = TypeAdapter(Union[
    SensorNameChange,
    SensorButtonEvent,
    TempHumiditySensor,
    SensorBatteryLevel,
    SensorPing,
    ButtonConfig,
    DaylightSensor,
    LightPing,
    LightStateChange,
    GroupStateChange,
])