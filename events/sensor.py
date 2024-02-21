from datetime import datetime
from typing import Any, List, Literal, Optional, Union

from .common import Base, MyBase, HeartbeatAttr


class ButtonState(MyBase):
    buttonevent: Optional[int]
    lastupdated: Union[datetime, Literal["none"]]
    eventduration: Optional[int] = None


class SensorButtonConfig(MyBase):
    clickmode: str
    devicemode: str
    on: bool
    reachable: bool


class SensorBatteryConfig(MyBase):
    alert: Optional[str] = None
    battery: int
    on: bool
    reachable: Optional[bool]
    offset: Optional[int] = None
    group: Optional[int] = None


class TempSensorState(MyBase):
    temperature: int
    lastupdated: datetime


class HumiditySensorState(MyBase):
    humidity: int
    lastupdated: datetime


class DaylightSensorState(MyBase):
    dark: bool
    daylight: bool
    status: int
    sunrise: datetime
    sunset: datetime
    lastupdated: datetime


class PowerSensorState(MyBase):
    current: int
    lastupdated: datetime
    power: int
    voltage: int


class PowerSensorConsumptionState(MyBase):
    consumption: int
    lastupdated: datetime


class SensorAddDump(MyBase):
    id: int
    config: SensorBatteryConfig
    etag: str
    lastannounced: Optional[datetime]
    lastseen: datetime
    manufacturername: str
    mode: int
    modelid: str
    name: str
    productname: str
    state: ButtonState
    type: str
    uniqueid: str


class SensorBase(Base):
    r: Literal["sensors"]
    uniqueid: str


class SensorChanged(SensorBase):
    e: Literal["changed"]
    uniqueid: str
    state: Optional[
        Union[
            ButtonState,
            TempSensorState,
            HumiditySensorState,
            DaylightSensorState,
            PowerSensorState,
            PowerSensorConsumptionState,
        ]
    ] = None
    attr: Optional[HeartbeatAttr] = None
    config: Optional[Union[SensorBatteryConfig, SensorButtonConfig]] = None


class SensorAdded(SensorBase):
    e: Literal["added"]
    uniqueid: str
    sensor: SensorAddDump
